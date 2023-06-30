from django.contrib import admin
from .models import Subscribers, NewsletterMessage

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined',)
    list_filter = ["date_joined"]
    readonly_fields = ["date_joined"]


class NewsLetterMessegeAdmin(admin.ModelAdmin):
    list_display = ["title", "date_send"]
    readonly_fields = ["date_send"]

    



admin.site.register(NewsletterMessage, NewsLetterMessegeAdmin)
admin.site.register(Subscribers, SubscriberAdmin)
