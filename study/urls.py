from django.urls import path, include
from . import views

urlpatterns = [
    path('study/ru/', views.study_ru, name='study_ru'),
    path('study-card/<slug:slug>/ru/', views.study_card_ru, name='study_card_ru'),
    path('study/uz/', views.study_uz, name='study_uz'),
    path('study-card/<slug:slug>/uz/', views.study_card_uz, name='study_card_uz'),
]
