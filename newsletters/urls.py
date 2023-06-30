from django.urls import path
from. import  views



urlpatterns = [
    path('subscribers/',views.subscribers_user,name="subscribers"),
    path('unsubscribeNewsletter/<uidb64>/',
         views.UnsubscribeNewsLetterEmail.as_view(), name="unsubscribeNewsletterEmail"),
         
]
