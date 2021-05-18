from django.shortcuts import render
from .models import *
from study.models import Study
from news.models import News
from products.models import Product
from django.core.paginator import Paginator


def categories_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        context = {
            'lang': 'ru',
            'categories_0': Categories.objects.all()[:4],
            'categories_1': Categories.objects.all()[4:],
            'subcategories': SubCategories.objects.all(),
            'products': Product.objects.all()
        }
        return render(request, 'products/all_products.html', context=context)
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


def categories_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        context = {
            'lang': 'uz',
            'categories_0': Categories.objects.all()[:4],
            'categories_1': Categories.objects.all()[4:],
            'subcategories': SubCategories.objects.all(),
            'products': Product.objects.all()
        }
        return render(request, 'products/all_products.html', context=context)
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


def items_ru(request, slug):
    search_query = request.GET.get('search-ru')
    if not search_query:
        filter = request.GET.get('price')
        if filter == 'low':
            filtered = []
            products = Product.objects.all().order_by('-price')
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            context = {
                'lang': 'ru',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': filtered,
                'priced': 'yes'
            }
            return render(request, 'products/items.html', context=context)
        elif filter == 'high':
            filtered = []
            products = Product.objects.all().order_by('price')
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            context = {
                'lang': 'ru',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': filtered,
                'priced': 'yes'
            }
            return render(request, 'products/items.html', context=context)
        elif filter == 'all':
            filtered = []
            products = Product.objects.all()
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            paginator = Paginator(filtered, 16)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'lang': 'ru',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': page_obj,
                'priced': 'no'
            }
            return render(request, 'products/items.html', context=context)
        else:
            filtered = []
            products = Product.objects.all()
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            paginator = Paginator(filtered, 16)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'lang': 'ru',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': page_obj,
                'priced': 'no'
            }
            return render(request, 'products/items.html', context=context)
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


def items_uz(request, slug):
    search_query = request.GET.get('search-uz')
    if not search_query:
        filter = request.GET.get('price')
        if filter == 'low':
            filtered = []
            products = Product.objects.all().order_by('-price')
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            context = {
                'lang': 'uz',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': filtered,
                'priced': 'yes'
            }
            return render(request, 'products/items.html', context=context)
        elif filter == 'high':
            filtered = []
            products = Product.objects.all().order_by('price')
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            context = {
                'lang': 'uz',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': filtered,
                'priced': 'yes'
            }
            return render(request, 'products/items.html', context=context)
        elif filter == 'all':
            filtered = []
            products = Product.objects.all()
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            paginator = Paginator(filtered, 16)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'lang': 'uz',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': page_obj,
                'priced': 'no'
            }
            return render(request, 'products/items.html', context=context)
        else:
            filtered = []
            products = Product.objects.all()
            for product in products:
                if str(product.subcategory.name) == str(SubCategories.objects.filter(slug=slug)[0]):
                    filtered.append(product)
            paginator = Paginator(filtered, 16)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'lang': 'uz',
                'subcategory': SubCategories.objects.filter(slug=slug)[0],
                'products': page_obj,
                'priced': 'no'
            }
            return render(request, 'products/items.html', context=context)
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


def product_card_ru(request, slug):
    search_query = request.GET.get('search-ru')
    if not search_query:
        context = {
            'lang': 'ru',
            'subcategory': Product.objects.filter(slug=slug)[0].subcategory,
            'selected_product': Product.objects.filter(slug=slug)[0],
            'similar': Product.objects.filter(subcategory=Product.objects.filter(slug=slug)[0].subcategory)[:5],
        }
        return render(request, 'products/product_card.html', context=context)
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


def product_card_uz(request, slug):
    search_query = request.GET.get('search-uz')
    if not search_query:
        context = {
            'lang': 'uz',
            'subcategory': Product.objects.filter(slug=slug)[0].subcategory,
            'selected_product': Product.objects.filter(slug=slug)[0],
            'similar': Product.objects.filter(subcategory=Product.objects.filter(slug=slug)[0].subcategory)[:5],
            'similar': Product.objects.filter(subcategory=Product.objects.filter(slug=slug)[0].subcategory)[:5],
        }
        return render(request, 'products/product_card.html', context=context)
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

