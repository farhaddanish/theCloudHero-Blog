import threading
from django.views import View
from posts.models import ArticlePost
from django.http.response import HttpResponseRedirect
from accounts.models import Account
from django.shortcuts import redirect, render
from .forms import UserAccountForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import  render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
import sweetify
from.utils import generate_token


# for fasting email
class EmailThread (threading.Thread):
    def __init__(self, html_email):
        self.html_email = html_email
        threading.Thread.__init__(self)

    def run(self):
        return self.html_email.send()


@receiver(post_save, sender=ArticlePost)
def sendArticle_user(sender, instance, created, **kwargs):
    if created:
        message = instance.article_title
        describtion = instance.article_describtion
        catagories = instance.catagories.article_main_catagories
        slug = instance.slug
        sender = settings.EMAIL_HOST_USER
        user = Account.objects.filter(is_active=True, is_admin=False)

        for i in user:
            uid= urlsafe_base64_encode(force_bytes(i.pk))
            html_template = render_to_string('accounts/newArticleEmail.html', {
                'message': message,
                'descibtion': describtion,
                'slug': slug,
                'catagories': catagories,
                'uid':  uid,
                'token': generate_token.make_token(i)
            })
            text_content = strip_tags(html_template)
            html_email = EmailMultiAlternatives(
                "New Article",
                text_content,
                sender,
                [i.email]
            )
            html_email.attach_alternative(html_template, "text/html")
            EmailThread(html_email).start()


# Login user
valid = False


def login_user(request):
    global valid
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST["pass"]
        form = authenticate(request, email=email, password=password)
        if form is not None:
            valid = False
            login(request, form)
            sweetify.sweetalert(request, ' login successfull 😊',
                                icon="success", persistent="Ok")

            return HttpResponseRedirect("/")
        else:
            valid = True
            return HttpResponseRedirect(reverse("login"))

    else:
        return render(request, "accounts/login.html", {
            "valid": valid
        })


# signup user
def signup_user(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            user = Account.objects.get(email=email)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            html_content = render_to_string("accounts/verfication.html", {

                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)

            })
            text_content = strip_tags(html_content)
            html_email = EmailMultiAlternatives(
                "Verify your Email",
                text_content,
                settings.EMAIL_HOST_USER,
                [user.email])
            html_email.attach_alternative(html_content, "text/html")
            EmailThread(html_email).start()
            messages.add_message(request, messages.INFO,
                                 "Please verify your Email")
            return redirect('login')
    else:
        form = UserAccountForm()
    return render(request, "accounts/signup.html", {
        "form": form
    })


# activate email
class ActivateAccountView (View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.INFO,
                                 'accounts activated succsefully')
            return redirect('login')
        sweetify.error(request, 'Some error happend here ',
                       text="try again", icon="error", persistent="Ok")
        return redirect('signup')


# logout user
def logout_user(request, url):
    logout(request)
    sweetify.success(request, 'Logout successfull', text="😥",
                     icon="success", persistent="ok")
    if url == "/search/":
        return redirect('index')
    return redirect(url)


# unsubscribe account email
class UnsubscribeAccountEmail (View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.delete()
            return render(request, 'accounts/unsubscribe.html')

        return render(request, 'accounts/invalid.html')


