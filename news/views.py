from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from rossvik.dbwork import CommentWork
import datetime
from django.contrib import messages
import os
from news.models import News
from study.models import Study
from products.models import Product


# Create your views here.
def news_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        news = News.objects.all()
        paginator = Paginator(news.order_by('-id'), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        new_news = []
        for i in news:
            new_news.append(i)
        news_with_comments_count = {
            # new: comment count
        }
        news_with_comments = {
            # new: comment
        }
        for new in page_obj:
            news_with_comments[new] = []
            for comment in Comments.objects.filter(post=True):
                if new.title == comment.news.title:
                    news_with_comments[new].append(comment.comment)
        for new, comment in news_with_comments.items():
            news_with_comments_count[new] = len(comment)
        context = {
            'lang': 'ru',
            'news_with_comments_count': news_with_comments_count,
            'news': page_obj,
            'new_news': new_news[-10:],
        }
        return render(request, 'news/news.html', context=context)
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


def card_ru(request, news_slug):
    search_query = request.GET.get('search-ru')
    if not search_query:
        comments_object = CommentWork()
        new_id = ''
        for new in comments_object.show_table('news_news'):
            if new[3] == news_slug:
                new_id += str(new[0])
        data = {
            'comment': request.GET.get('message'),
            'author_name': request.GET.get('fname'),
            'author_mail': request.GET.get('email'),
            'site': request.GET.get('site'),
            'post': 0,
            'news': new_id
        }
        if not data['comment'] or not data['author_name'] or not data['author_mail']:
            pass
        else:
            comments_object.write_to_db(data=data, table='news_comments', datas='news')
            os.system(f'bot_engine/main.py -n "{data["author_name"]}" -e "{data["author_mail"]}" -s "{News.objects.get(slug=news_slug).title}" -m "{data["comment"]}" -o news_comments -w "{data["site"]}"')

        context = {
            'lang': 'ru',
            'news': News.objects.get(slug=news_slug),
            'images': Images.objects.all(),
            'comments': Comments.objects.filter(news_id=new_id, post=True)
        }
        if data['comment'] is not None:
            messages.success(request, "Ваш комментарий успешно отправлен, дождитесь подтверждения модератора")
        return render(request, 'news/news-card.html', context)
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


def news_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        news = News.objects.all()
        paginator = Paginator(news.order_by('-id'), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        new_news = []
        for i in news:
            new_news.append(i)
        news_with_comments_count = {
            # new: comment count
        }
        news_with_comments = {
            # new: comment
        }
        for new in page_obj:
            news_with_comments[new] = []
            for comment in Comments.objects.filter(post=True):
                if new.title == comment.news.title:
                    news_with_comments[new].append(comment.comment)
        for new, comment in news_with_comments.items():
            news_with_comments_count[new] = len(comment)
        context = {
            'lang': 'uz',
            'news_with_comments_count': news_with_comments_count,
            'news': page_obj,
            'new_news': new_news[-10:],
        }
        return render(request, 'news/news.html', context=context)
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


def card_uz(request, news_slug):
    search_query = request.GET.get('search-uz')
    if not search_query:
        comments_object = CommentWork()
        new_id = ''
        for new in comments_object.show_table('news_news'):
            if new[3] == news_slug:
                new_id += str(new[0])
        data = {
            'comment': request.GET.get('message'),
            'author_name': request.GET.get('fname'),
            'author_mail': request.GET.get('email'),
            'site': request.GET.get('site'),
            'post': 0,
            'news': new_id
        }
        if not data['comment'] or not data['author_name'] or not data['author_mail']:
            pass
        else:
            comments_object.write_to_db(data=data, table='news_comments', datas='news')
            os.system(f'bot_engine/main.py -n "{data["author_name"]}" -e "{data["author_mail"]}" -s "{News.objects.get(slug=news_slug).title}" -m "{data["comment"]}" -o news_comments -w "{data["site"]}"')

        context = {
            'lang': 'uz',
            'news': News.objects.get(slug=news_slug),
            'images': Images.objects.all(),
            'comments': Comments.objects.filter(news_id=new_id, post=True)
        }
        if data['comment'] is not None:
            messages.success(request, "Sizning xabaringiz yuborildi, tasdiqlanish jarayonini kutib turing")
        return render(request, 'news/news-card.html', context)
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
