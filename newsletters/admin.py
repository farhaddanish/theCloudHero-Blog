from django.contrib import admin
from .models import Subscribers, NewsletterMessage
# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined',)
    list_filter = ["date_joined"]
    readonly_fields = ["date_joined"]


class MailMessageAdmin (admin.ModelAdmin):
    list_display = ["title", "date_send"]
    readonly_fields = ["date_send"]


admin.site.register(Subscribers, NewsletterAdmin)
admin.site.register(NewsletterMessage, MailMessageAdmin)
