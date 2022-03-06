from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('index/', views.index),
    path('articles/', views.articles, name='articles'),
    path('article/<int:id>/', views.article_detail_view)
]