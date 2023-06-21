import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mainApp.settings')
import django
django.setup()

import random
from posts.models import ArticlePost, ArticleAuthor, ArticleCaption, ArticleMainCatagories
from faker import Faker

fakgen = Faker()
main = ['Windows', 'Server', 'Cloud', 'Storage', 'SharePoint', 'Office']


def articleMain():
    objectOfMain = ArticleMainCatagories.objects.get_or_create(
        article_main_catagories=random.choice(main))[0]
    objectOfMain.save()
    return objectOfMain



# def articleAuthor ():
#     author = 0
#     for i in range(10):
#         fake_person = fakgen.name()
#         fake_person_last =fakgen.name()
#         author = ArticleAuthor.objects.get_or_create(FirstName=fake_person,LastName=fake_person_last)[0]
#         author.save()
    
#     return author



def articleCaption():
    caption = ArticleCaption.objects.get_or_create(caption = "News")[0]
    caption.save()
    return caption 




def posts (n=5):
    caption = articleCaption()
    author = ArticleAuthor.objects.get_or_create(FirstName="ahmad",LastName="farid")[0]
    author.save()
    catagories = articleMain()
    
    for i in range(n):
        title = fakgen.name()
        date =fakgen.date()
        describe =  fakgen.text()
        content = fakgen.text()
        # image = fakgen.image()
        slug = fakgen.slug()


        a = ArticlePost.objects.get_or_create(article_title = title,article_caption=caption, article_author =author,
            post_date = date,article_describtion = describe,catagories =  catagories,
            article_content1 = content,article_content2 = content,article_content3 =content, slug=slug)[0]
        a.save()



if __name__  == '__main__':
    print('start')
    posts(245)
    print('finish')







# for account views

# send automate email
# @receiver(post_save, sender=ArticlePost)
# def sendArticle_user(sender, instance, created, **kwargs):
#     if created:
#         message = instance.article_title
#         describtion = instance.article_describtion
#         catagories = instance.catagories.article_main_catagories
#         slug = instance.slug

#         sender = settings.EMAIL_HOST_USER
#         user = Account.objects.filter(is_active=True, is_admin=False)
#         for i in user:
#             html_content = render_to_string("accounts/newArticleEmail.html", {
#                 'user' : i.email,
#                 'message': message,
#                 'descibtion': describtion,
#                 'slug': slug,
#                 'catagories': catagories,

#             })
#             text_content = strip_tags(html_content)
#             html_email = EmailMultiAlternatives(
#                 "New Article",
#                 text_content,
#                 sender,
#                 [i.email])
#             html_email.attach_alternative(html_content, "text/html")
#         # html_email.send()
#             EmailThread(html_email).start()


# email = EmailMultiAlternatives()
        # email.subject = "New Article"
        # email.from_email = sender
        # email.bcc = [i.email]
        # email.body = body.replace('{email}',i.email)
        # email.attach_alternative(body.replace('{email}',i.email),"text/html")
        # email.connection= connection
        # email.send()
        # EmailThread(email).start()

        # connection.close()





#  for newsletter views



# def unsubscribers_user(request,email):
#     user = Subscribers.objects.get(email=email)
#     user.delete()
#     sweetify.success(request,"Unsubscribed Successfull", Text="you will not recieve cool newsletter",persistent="ok")
#     return HttpResponseRedirect('/')
    # if request.method == "POST" and request.is_ajax():
    #     form = SubscribersForm(request.POST or None)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         if Subscribers.objects.filter(email=instance.email).exist():
    #             Subscribers.objects.filter(email=instance.email).delete()

    #             return JsonResponse({
    #                 "unsubscribe": True
    #             })

    #         else:
    #             return JsonResponse({
    #                 "UserNotFound": True
    #             })


# @receiver(post_save, sender=MailMessage)
# def sendArticle_user(sender, instance, created, **kwargs):
#     if created:
#         toUser = Subscribers.objects.all()
#         title = instance.title
#         message = instance.message
#         date = instance.date_send
#         sender = settings.EMAIL_HOST_USER
#         context = {

#             'title': title,
#             'message': message,
#             'date': date,
#         }
#         template  = get_template("newsletters/newsletter.html")
#         body = template.render(context)

#         for i in toUser:
#             html_email = EmailMultiAlternatives(
#                 "theCloudHeros Newsletter",
#                 # body.replace('{email}',i.email),
#                 body.replace('{uid}', urlsafe_base64_encode(force_bytes(i.pk))),
#                 sender,
#                 [i.email])
#             html_email.attach_alternative(body.replace('{uid}', urlsafe_base64_encode(force_bytes(i.pk))), "text/html")
#             EmailThread(html_email).start()


# with open('C:\\Users\\Farhad Danish\\Desktop\\theCloudHeros-Backend\\mainApp\\uploads\\'+image , mode='rb') as f:
        #     imagefile = MIMEImage(f.read())
        #     html_email.attach(imagefile)
        #     # imagefile.add_header('Content-ID',f"<test image>")
        # html_email.send()

        # with smtplib.SMTP('smtp.gmail.com',port) as mail:
        #     mail.ehlo()
        #     mail.starttls()
        #     mail.ehlo()
        #     mail.login(sender,password)
        #     msg = f'Subject : {title} \n\n {message}'
        #     for email in Subscribers.objects.all():
        #         mail.sendmail(sender,email.email,msg)
