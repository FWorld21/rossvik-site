from django.shortcuts import render
from . models import *
from study.models import Study
from news.models import News
from products.models import Product


def about_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        about = About.objects.all()
        context = {
            'lang': 'ru',
            'news': about,
        }
        return render(request, 'about/about.html', context=context)
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


def about_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        about = About.objects.all()
        context = {
            'lang': 'uz',
            'news': about,
        }
        return render(request, 'about/about.html', context=context)
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

