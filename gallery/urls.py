from django.urls import path, include
from . import views

urlpatterns = [
    path('gallery/ru/', views.gallery_ru, name='gallery_ru'),
    path('gallery/uz/', views.gallery_uz, name='gallery_uz'),
]
