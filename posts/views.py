from django.http.response import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import ArticlePost, ArticleMainCatagories
from django.contrib.auth import authenticate,  login
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# https://localhost:8000
def index(request):
    p = Paginator(ArticlePost.objects.all().order_by('-post_date'), 15)
    nav = ArticleMainCatagories.objects.all()
    page = request.GET.get('page')
    venus = p.get_page(page)
    return render(request, "posts/index.html", {
        "venus": venus,
        "nav": nav
    })


# https://localhost:8000/windows
def catagoriesPart(request, text):
    month = 1
    catagoriesfilter = ArticleMainCatagories.objects.filter(
        article_main_catagories__icontains=text).exists()
    if not catagoriesfilter:
        raise Http404

    p = Paginator(ArticlePost.objects.filter(
        catagories__article_main_catagories__icontains=text).order_by('-post_date'), 10)
    page = request.GET.get('page')
    venus = p.get_page(page)

    earlier = ArticlePost.objects.filter(
        catagories__article_main_catagories__icontains=text, post_date__month__lte=month).order_by('?')[:5]

    nav = ArticleMainCatagories.objects.all()

    return render(request, "posts/post-catagories.html", {
        "catagories": text.lower(),
        "posts": venus,
        "earlier": earlier,
        "nav": nav

    })


# https://localhost:8000/windows/slug
def articleDetails(request, string, slug):
    catagoriesFilter = ArticleMainCatagories.objects.filter(
        article_main_catagories__icontains=string).exists()
    if not catagoriesFilter:
        raise Http404

    posts = get_object_or_404(ArticlePost, slug=slug)
    query = Q()

    for i in posts.article_title.split():
        query = query | Q(article_title__icontains=i)

    related = ArticlePost.objects.filter(query).filter(
        catagories__article_main_catagories__icontains=string).exclude(slug__exact=slug)[:5]

    nav = ArticleMainCatagories.objects.all()

    return render(request, "posts/articleDetails.html", {
        "posts": posts,
        "related": related,
        "nav": nav

    })


# catagories/windows
def ArticleSubPart(request, string2):
    month = 1
    catagoriesFilter = ArticleMainCatagories.objects.filter(
        article_main_catagories__icontains=string2).exists()
    if not catagoriesFilter:
        raise Http404

    p = Paginator(ArticlePost.objects.filter(
        catagories__article_main_catagories__icontains=string2).order_by('-post_date'), 10)
    page = request.GET.get('page')
    venus = p.get_page(page)

    nav = ArticleMainCatagories.objects.all()

    earlier = ArticlePost.objects.filter(
        catagories__article_main_catagories__icontains=string2, post_date__month__lte=month).order_by('?')[:5]
    return render(request, "posts/post-catagories.html", {
        "catagories": string2.lower(),
        "posts": venus,
        "earlier": earlier,
        "nav": nav

    })


# catagories/windows/windows-8
def articleSubCatagoriePart(request, text2, slug2):
    month = 1
    catagoriesFilter = ArticleMainCatagories.objects.filter(
        article_sub_catagories__slug__iexact=slug2, article_main_catagories__icontains=text2).exists()
    if not catagoriesFilter:
        raise Http404

    p = Paginator(ArticlePost.objects.filter(
        sub_catagories__slug__icontains=slug2).order_by('-post_date'), 10)
    page = request.GET.get('page')
    venus = p.get_page(page)

    nav = ArticleMainCatagories.objects.all()

    earlier = ArticlePost.objects.filter(
        catagories__article_main_catagories__icontains=text2, post_date__month__lte=month).order_by('?')[:5]
    return render(request, "posts/post-catagories.html", {
        "catagories": slug2.lower(),
        "posts": venus,
        "earlier": earlier,
        "nav": nav

    })


# privacy/
def privacy(request):
    nav = ArticleMainCatagories.objects.all()
    return render(request, "posts/privacy.html", {
        "nav": nav
    })


# searching
def searchFunction(request):
    if request.method == 'GET':
        nav = ArticleMainCatagories.objects.all()
        serach_text = request.GET.get('search')

        # try:
        if serach_text:
            posts = ArticlePost.objects.filter(
                article_title__icontains=serach_text)
        p = Paginator(posts.order_by('-post_date'), 20)
        page = request.GET.get('page')
        try:
            venus = p.page(page)
        except PageNotAnInteger:
            venus = p.page(1)
        except EmptyPage:
            venus = p.page(p.num_pages)

        return render(request, 'posts/search.html', {
            "venus": venus,
            "searchText": serach_text,
            "nav": nav,
            "query": serach_text
        })


# ajxa Login
def ajaxLogin(request):
    if request.method == "POST" and request.is_ajax():
        email = request.POST.get('email')
        
        password = request.POST.get('password')
        form = authenticate(request, email=email, password=password)
        if form is not None:
            login(request, form)
            return JsonResponse({
                "login": True
            })
        else:
            return JsonResponse({
                "Login": False
            })
