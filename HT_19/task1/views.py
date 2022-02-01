# 1. Пройти туторіал по Джанго (частини 1, 2, 3).https://docs.djangoproject.com/en/4.0/
# 2. На основі скрейпера із попередньої ДЗ створити сайт:
#  1. Основна сторінка - одна. На ній - дропдаун із доступними категоріями і кнопка.
# По натисканню на неї відбувається скрейпінг вибраної категорії.
# 2. Кожен тип записів (Ask, Job, Story) - це окрема модель зі своїми полями.
# 3. По полям типа "kids", "parents", "coments" та подібним ітеруватись не потрібно.
# 4. Під час скрейпінга скачувати тільки ті записи, яких немає в базі.
# 5. Всі записи виводити в Адмінці (зараз не потрібно створювати для них окремі сторінки в UI).

import requests

from tqdm import tqdm

from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render

from .models import Askstor, Jobstor, Showstor, Newstor


def get_ids_list(user_choice):
    categ_url = f'https://hacker-news.firebaseio.com/v0/{user_choice}.json'
    category_list = requests.get(url=categ_url).json()
    return category_list


def create_list_categories(drop_category):
    article_dicts_list = []
    category_articles = get_ids_list(drop_category)

    for article in tqdm(category_articles):
        article_on_id = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
        req_article_dict = requests.get(url=article_on_id).json()
        article_dicts_list.append(req_article_dict)
        print(article_dicts_list)

    return article_dicts_list


def show_index_page(request):

    category = request.POST.get('choices_category')
    artic_list = create_list_categories(category)

    if category == 'askstories':
        askstor(artic_list)
    elif category == 'jobstories':
        jobstor(artic_list)
    elif category == 'newstories':
        newstor(artic_list)
    elif category == 'showstories':
        showstor(artic_list)
    return render(request, 'task1/index.html')

def askstor(articles_list):

    for item in articles_list:
        try:
            table_ask = Askstor.objects.create(
                by=item['by'],
                descendants=item['descendants'],
                id_ask=item['id'],
                score=item['score'],
                text=item.get('text', ''),
                time=item['time'],
                title=item['title'],
                type=item['type']
            )
            table_ask.save()

        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                print('This item already exists.')

    return HttpResponse('Your request has been completed! Go to the admin panel!')

def jobstor(articles_list):

    for item in articles_list:

        try:
            table_job = Jobstor.objects.create(
                by=item['by'],
                id_job=item['id'],
                score=item.get('score', ''),
                text=item.get('text', ''),
                time=item['time'],
                title=item['title'],
                type=item['type'],
                url=item.get('url', '')
            )
            table_job.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                print('This item already exists.')

    return HttpResponse('Your request has been completed! Go to the admin panel!')

def newstor(articles_list):

    for item in articles_list:

        try:
            table_new = Newstor.objects.create(
                by=item['by'],
                descendants=item['descendants'],
                id_new=item['id'],
                score=item['score'],
                time=item['time'],
                title=item['title'],
                type=item['type'],
                url=item.get('url', ''),
                text=item.get('text', '')
            )
            table_new.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                print('This item already exists.')

    return HttpResponse('Your request has been completed! Go to the admin panel!')

def showstor(articles_list):

    for item in articles_list:

        try:
            table_show = Showstor.objects.create(
                by=item['by'],
                descendants=item['descendants'],
                id_show=item['id'],
                score=item['score'],
                text=item.get('text', ''),
                time=item['time'],
                title=item['title'],
                type=item['type'],
                url=item.get('url', ''),

            )
            table_show.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                print('This item already exists.')

    return HttpResponse('Your request has been completed! Go to the admin panel!')


