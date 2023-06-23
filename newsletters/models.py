from django.db import models
from .fields import LowerEmailField


# subscribers
class Subscribers(models.Model):
    email = LowerEmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribers"



# Mail message
class NewsletterMessage (models.Model):
    title = models.CharField(max_length=100, null=True)
    date_send = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "NewsLetter Messages"
