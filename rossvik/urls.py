"""rossvik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import search_ru, search_uz

urlpatterns = [
    path('', include('products.urls'), name='products_ru'),
    path('', include('gallery.urls'), name='gallery_ru'),
    path('', include('news.urls'), name='news_ru'),
    path('', include('study.urls'), name='study_ru'),
    path('', include('study.urls'), name='study_card_ru'),
    path('', include('about.urls'), name='about_ru'),
    path('', include('contacts.urls'), name='contacts_ru'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
