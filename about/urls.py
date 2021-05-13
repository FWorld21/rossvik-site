from django.urls import path, include
from . import views

urlpatterns = [
    path('about/ru/', views.about_ru, name='about_ru'),
    path('about/uz/', views.about_uz, name='about_uz'),
]
