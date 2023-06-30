from django.urls import path
from . import views

urlpatterns = [
    path('logout/<path:url>/', views.logout_user, name="logout"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup_user, name="signup"),
    path('unsubscribeAccount/<uidb64>/<token>/',
         views.UnsubscribeAccountEmail.as_view(), name="unsubscribeAccountEmail"),
    path('activate/<uidb64>/<token>/',
         views.ActivateAccountView.as_view(), name="activate"),

]
