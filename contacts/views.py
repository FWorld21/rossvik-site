from django.shortcuts import render
from .models import *
import os
from study.models import Study
from news.models import News
from products.models import Product


def contacts_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        data = {
            'name': request.GET.get('name'),
            'email': request.GET.get('email'),
            'subject': request.GET.get('subject'),
            'message': request.GET.get('message'),
        }
        if not data['name'] or not data['message'] or not data['email']:
            pass
        else:
            os.system(f'bot_engine/main.py -n "{data["name"]}" -e "{data["email"]}" -s "{data["subject"]}" -m "{data["message"]}" -o question')

        contacts = Contacts.objects.all()
        context = {
            'lang': 'ru',
            'categories': contacts
        }
        return render(request, 'contacts/contacts.html', context=context)
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


def contacts_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        data = {
            'name': request.GET.get('name'),
            'email': request.GET.get('email'),
            'subject': request.GET.get('subject'),
            'message': request.GET.get('message'),
        }
        if not data['name'] or not data['message'] or not data['email']:
            pass
        else:
            os.system(f'bot_engine/main.py -n "{data["name"]}" -e "{data["email"]}" -s "{data["subject"]}" -m "{data["message"]}" -o question')

        contacts = Contacts.objects.all()
        context = {
            'lang': 'uz',
            'categories': contacts
        }
        return render(request, 'contacts/contacts.html', context=context)
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
