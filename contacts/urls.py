from django.urls import path, include
from . import views

urlpatterns = [
    path('contacts/ru', views.contacts_ru, name='contacts_ru'),
    path('contacts/uz', views.contacts_uz, name='contacts_uz'),
]
