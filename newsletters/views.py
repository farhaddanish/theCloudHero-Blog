from .models import Subscribers, NewsletterMessage
from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.views import View
import threading
import sweetify


# for fasting email
class EmailThread (threading.Thread):
    def __init__(self, html_email):
        self.html_email = html_email
        threading.Thread.__init__(self)

    def run(self):
        return self.html_email.send()


# automate to subscribers

@receiver(post_save, sender=NewsletterMessage)
def sendArticle_user(sender, instance, created, **kwargs):
    if created:
        toUser = Subscribers.objects.all()
        title = instance.title
        message = instance.message
        date = instance.date_send
        sender = settings.EMAIL_HOST_USER

        for i in toUser:
            uid = urlsafe_base64_encode(force_bytes(i.pk))
            html_content = render_to_string("newsletters/newsletter.html", {

                'title': title,
                'message': message,
                'date': date,
                'uid': uid

            })
            text_content = strip_tags(html_content)
            html_email = EmailMultiAlternatives(
                "theCloudHeros Newsletter",
                text_content,
                sender,
                [i.email])

            html_email.attach_alternative(html_content, "text/html")
            EmailThread(html_email).start()


# subscribe user
def subscribers_user(request):
    if request.method == "POST" and request.is_ajax():
        email = request.POST['email']
        if Subscribers.objects.filter(email=email).exists():
            return JsonResponse({
                    "userExist": True
                })
        else:
            Subscribers.objects.create(email=email)
            return JsonResponse({
                "subscribed": True,
            })
        


# unsubscribe account email
class UnsubscribeNewsLetterEmail (View):
    def get(self, request, uidb64):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Subscribers.objects.get(pk=uid)
        except Exception as identifier:
            user = None

        if user is not None:
            user.delete()
            return render(request, 'newsletters/unsubscribe.html')

        return render(request, 'newsletters/invalid.html')


