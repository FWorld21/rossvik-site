from django.urls import path, include
from . import views

urlpatterns = [
    path('news/ru/', views.news_ru, name='news_ru'),
    path('news/<slug:news_slug>/ru/', views.card_ru, name='news_card_ru'),

    path('news/uz/', views.news_uz, name='news_uz'),
    path('news/<slug:news_slug>/uz/', views.card_uz, name='news_card_uz'),
]
