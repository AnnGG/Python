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
    print(category_list)
    return category_list


def create_list_categories(drop_category, l_id):

    article_dicts_list = []
    category_articles = get_ids_list(drop_category)


    for article in tqdm(category_articles):
        if article not in l_id:
            article_on_id = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
            req_article_dict = requests.get(url=article_on_id).json()
            if req_article_dict is not None:
                article_dicts_list.append(req_article_dict)

    print(len(category_articles))
    print(len(article_dicts_list))

    if len(article_dicts_list) == 0:
        print("There were no new stories today!")

    return article_dicts_list


def show_index_page(request):

    category = request.POST.get('choices_category')

    if category == 'askstories':
        list_id = Askstor.objects.all().values_list('id_ask', flat=True)
        artic_list = create_list_categories(category, list_id)
        askstor(artic_list)

    elif category == 'jobstories':
        list_id = Jobstor.objects.all().values_list('id', flat=True)
        artic_list = create_list_categories(category, list_id)
        jobstor(artic_list)

    elif category == 'newstories':
        list_id = Newstor.objects.all().values_list('id', flat=True)
        artic_list = create_list_categories(category, list_id)
        newstor(artic_list)

    elif category == 'showstories':
        list_id = Showstor.objects.all().values_list('id', flat=True)
        artic_list = create_list_categories(category, list_id)
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
                id=item.get('id', ''),
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
                descendants=item.get('descendants', ''),
                id=item.get('id', ''),
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
                descendants=item.get('descendants', ''),
                id=item['id'],
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
