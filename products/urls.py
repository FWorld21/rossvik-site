from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.categories_ru, name='products_ru'),
    path('uz/', views.categories_uz, name='products_uz'),
    path('categories/<slug:slug>/ru/', views.items_ru, name='items_ru'),
    path('categories/<slug:slug>/uz/', views.items_uz, name='items_uz'),
    path('products/<slug:slug>/ru/', views.product_card_ru, name='product_card_ru'),
    path('products/<slug:slug>/uz/', views.product_card_uz, name='product_card_uz'),
]