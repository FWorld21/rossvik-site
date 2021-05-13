from django.core.paginator import Paginator
from django.shortcuts import render
from news.models import News
from study.models import Study
from products.models import Product
from .models import *


def gallery_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        paginator = Paginator(Post.objects.all().order_by('-id'), 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        news = News.objects.all()
        new_news = []
        for i in news:
            new_news.append(i)
        context = {
            'lang': 'ru',
            'posts': page_obj,
            'images': Images.objects.all(),
            'new_news': new_news[-10:],
        }
        return render(request, 'gallery/gallery.html', context=context)
    else:
        study_queryset = []
        news_queryset = []
        products_queryset = []
        for study in Study.objects.all():
            if search_query in study.title.lower():
                study_queryset.append(study)
        for new in News.objects.all():
            if search_query in new.title.lower():
                news_queryset.append(new)
        for product in Product.objects.all():
            if search_query in product.name.lower():
                products_queryset.append(product)
        context = {
            'lang': 'ru',
            'search_word': search_query,
            'study': study_queryset,
            'news': news_queryset,
            'products': products_queryset,
        }
        return render(request, 'rossvik/search.html', context=context)


def gallery_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        paginator = Paginator(Post.objects.all().order_by('-id'), 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        news = News.objects.all()
        new_news = []
        for i in news:
            new_news.append(i)
        context = {
            'lang': 'uz',
            'posts': page_obj,
            'images': Images.objects.all(),
            'new_news': new_news[-10:],
        }
        return render(request, 'gallery/gallery.html', context=context)
    else:
        study_queryset = []
        news_queryset = []
        products_queryset = []
        for study in Study.objects.all():
            if search_query in study.title.lower():
                study_queryset.append(study)
        for new in News.objects.all():
            if search_query in new.title.lower():
                news_queryset.append(new)
        for product in Product.objects.all():
            if search_query in product.name.lower():
                products_queryset.append(product)
        context = {
            'lang': 'uz',
            'search_word': search_query,
            'study': study_queryset,
            'news': news_queryset,
            'products': products_queryset,
        }
        return render(request, 'rossvik/search.html', context=context)