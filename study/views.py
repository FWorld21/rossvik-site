from django.core.paginator import Paginator
from django.shortcuts import render
from study.models import Study
from news.models import News
from products.models import Product
from rossvik.dbwork import CommentWork
from django.contrib import messages
from . models import *
import os


def study_ru(request):
    search_query = request.GET.get('search-ru')
    if not search_query:
        study = Study.objects.all()
        paginator = Paginator(study.order_by('-id'), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        news = News.objects.all()
        new_news = []
        for i in news:
            new_news.append(i)
        study_with_comments_count = {
            # new: comment count
        }
        study_with_comments = {
            # new: comment
        }
        for stud in page_obj:
            study_with_comments[stud] = []
            for comment in Comments.objects.filter(post=True):
                if stud.title == comment.study.title:
                    study_with_comments[stud].append(comment.comment)
        for stud, comment in study_with_comments.items():
            study_with_comments_count[stud] = len(comment)
        context = {
            'lang': 'ru',
            'study_with_comments_count': study_with_comments_count,
            'studies': page_obj,
            'new_news': new_news[-10:],
        }
        return render(request, 'study/study.html', context=context)
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


def study_card_ru(request, slug):
    search_query = request.GET.get('search-ru')
    if not search_query:
        comments_object = CommentWork()
        study_id = ''
        for new in comments_object.show_table('study_study'):
            if new[3] == slug:
                study_id += str(new[0])
        data = {
            'comment': request.GET.get('message'),
            'author_name': request.GET.get('fname'),
            'author_mail': request.GET.get('email'),
            'site': request.GET.get('site'),
            'post': 0,
            'study': study_id
        }
        if not data['comment'] or not data['author_name'] or not data['author_mail']:
            pass
        else:
            comments_object.write_to_db(data=data, table='study_comments', datas='study')
            os.system(f'bot_engine/main.py -n "{data["author_name"]}" -e "{data["author_mail"]}" -s "{Study.objects.get(slug=slug).title}" -m "{data["comment"]}" -o study_comments -w "{data["site"]}"')


        context = {
            'lang': 'ru',
            'study': Study.objects.get(slug=slug),
            'images': Images.objects.all(),
            'comments': Comments.objects.filter(study_id=study_id, post=True)
        }
        if data['comment'] is not None:
            messages.success(request, "Ваш комментарий успешно отправлен, дождитесь подтверждения модератора")
        return render(request, 'study/study-card.html', context=context)
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


def study_uz(request):
    search_query = request.GET.get('search-uz')
    if not search_query:
        study = Study.objects.all()
        paginator = Paginator(study.order_by('-id'), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        news = News.objects.all()
        new_news = []
        for i in news:
            new_news.append(i)
        study_with_comments_count = {
            # new: comment count
        }
        study_with_comments = {
            # new: comment
        }
        for stud in page_obj:
            study_with_comments[stud] = []
            for comment in Comments.objects.filter(post=True):
                if stud.title == comment.study.title:
                    study_with_comments[stud].append(comment.comment)
        for stud, comment in study_with_comments.items():
            study_with_comments_count[stud] = len(comment)
        context = {
            'lang': 'uz',
            'study_with_comments_count': study_with_comments_count,
            'studies': page_obj,
            'new_news': new_news[-10:],
        }
        return render(request, 'study/study.html', context=context)
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


def study_card_uz(request, slug):
    search_query = request.GET.get('search-uz')
    if not search_query:
        comments_object = CommentWork()
        study_id = ''
        for new in comments_object.show_table('study_study'):
            if new[3] == slug:
                study_id += str(new[0])
        data = {
            'comment': request.GET.get('message'),
            'author_name': request.GET.get('fname'),
            'author_mail': request.GET.get('email'),
            'site': request.GET.get('site'),
            'post': 0,
            'study': study_id
        }
        if not data['comment'] or not data['author_name'] or not data['author_mail']:
            pass
        else:
            comments_object.write_to_db(data=data, table='study_comments', datas='study')
            os.system(f'bot_engine/main.py -n "{data["author_name"]}" -e "{data["author_mail"]}" -s "{Study.objects.get(slug=slug).title}" -m "{data["comment"]}" -o study_comments -w "{data["site"]}"')


        context = {
            'lang': 'uz',
            'study': Study.objects.get(slug=slug),
            'images': Images.objects.all(),
            'comments': Comments.objects.filter(study_id=study_id, post=True)
        }
        if data['comment'] is not None:
            messages.success(request, "Sizning xabaringiz yuborildi, tasdiqlanish jarayonini kutib turing")
        return render(request, 'study/study-card.html', context=context)
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