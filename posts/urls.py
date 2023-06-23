from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.searchFunction, name="search"),
    path('privacypolicy/', views.privacy, name="privacy"),
    path('<str:text>/', views.catagoriesPart, name="catagoriesPart"),
    path('catagories/<str:string2>/', views.ArticleSubPart, name="ArticleSubPart"),
    path('<str:string>/<slug:slug>/', views.articleDetails, name="articleDetails"),
    path('catagories/<str:text2>/<slug:slug2>/',
         views.articleSubCatagoriePart, name="SubCatagoriesPart"),

    path('loginWithAjax', views.ajaxLogin, name="ajaxLogin"),

]
