# Написати програму, яка буде робити наступне:
# 1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
# 2. Запропонувати обрати користувача (ввести ID)
# 3. Розробити наступну менюшку (із вкладеними пунктами):
#    1. Повна інформація про користувача
#    2. Пости:
#       - перелік постів користувача (ID та заголовок)
#       - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
#    3. ТУДУшка:
#       - список невиконаних задач
#       - список виконаних задач
#    4. Вивести URL рандомної картинки


import random
import requests
import json


def get_connect():

    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = response_users.text
    parse_users_data_json = json.loads(users_data)
    return parse_users_data_json


def get_user_id_name_nik():

    print('-' * 40)
    key_list = ['id', 'name', 'username']
    for users in get_connect():
        for user_keys in users:
            if user_keys in key_list:
                print(user_keys, ": ", users[user_keys])
        print('-' * 40)


def get_user_on_id(id_parametr):

    print('-' * 40)
    for users in get_connect():
        if users['id'] == id_parametr:
            print('id:', users['id'])
            print('name:', users['name'])
            print('username:', users['username'])
            print('email:', users['email'])
            for user_items, user_val in users['address'].items():
                if user_items != 'geo':
                    print(user_items, ":", user_val)
            for user_items, user_val in users['address']['geo'].items():
                print(user_items, ":", user_val)
            print('phone:', users['phone'])
            print('website:', users['website'])
            for user_items, user_val in users['company'].items():
                print(user_items, ":", user_val)

    print('-' * 40)

def info_user_post(id_user_parametr):

    print('-' * 40)
    response_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_data = response_posts.text
    parse_posts_data_json = json.loads(posts_data)

    for users_posts in parse_posts_data_json:
        if users_posts['userId'] == id_user_parametr:
            print(users_posts['id'], ":", users_posts['title'])
    print("-" * 20, "List tasks", "-" * 20)

def info_post_on_id(id_post_parametr):

    print('-' * 40)
    response_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_data = response_posts.text
    parse_posts_data_json = json.loads(posts_data)
    response_coments = requests.get('https://jsonplaceholder.typicode.com/comments')
    coments_data = response_coments.text
    parse_coments_data_json = json.loads(coments_data)
    count_coment = 0
    for users_posts in parse_posts_data_json:
        if users_posts['id'] == id_post_parametr:
            print("user_id: ", users_posts['userId'])
            print(users_posts['id'], ":", users_posts['title'])
            print(users_posts['body'])
    for users_coments in parse_coments_data_json:
        if users_coments['postId'] == id_post_parametr:
            count_coment += 1
            print("id_coments:", users_coments['id'], end=" ")
    print('\ncount:', count_coment)
    print('-' * 40)


def todo_list(user_id_param, todo_parametr):

    print("-" * 20, "List tasks", "-" * 20)
    response_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = response_todo.text
    parse_todo_data_json = json.loads(todos_data)

    if todo_parametr == 1:
        todo_parametr = True
    elif todo_parametr == 2:
        todo_parametr = False

    for items in parse_todo_data_json:
        if items['userId'] == user_id_param:
            if items['completed'] == todo_parametr:
                print(items['id'], ":", items['title'])
    print('-' * 40)


def url_picture():

    print("-" * 40)
    response_foto = requests.get('https://jsonplaceholder.typicode.com/photos')
    foto_data = response_foto.text
    parse_foto_data_json = json.loads(foto_data)

    random_foto_id = random.randint(1, 5000) + 1
    for items in parse_foto_data_json:
        if items['id'] == random_foto_id:
            print('url: ', items['url'])
    print('-' * 40)


class NotFoundUser(object):
    pass


def user_response():

    print("-" * 20, "Menu", "-" * 20)
    while True:
        print(' 1 - Get short information about a user.'
              '\n 2 - Get information about a user on id'
              '\n 3 - User posts information'
              '\n 4 - Posts information on id'
              '\n 5 - Todo info'
              '\n 6 - Url picture'
              '\n 7 - Exit')

        user_option = input('Select an option: ')

        if user_option == '1':
            get_user_id_name_nik()

        elif user_option == '2':
            user_response_parametr = int(input("Input id user: "))
            get_user_on_id(user_response_parametr)


        elif user_option == '3':
            user_id_param = int(input("Input id user: "))
            info_user_post(user_id_param)

        elif user_option == '4':
            user_id_post = int(input("Input post id: "))
            info_post_on_id(user_id_post)

        elif user_option == '5':
            user_res_param = int(input("Input user id: "))
            todo_response_parametr = int(input("Press 1/2 to check completed / failed tasks: "))
            todo_list(user_res_param, todo_response_parametr)

        elif user_option == '6':
            url_picture()

        else:
            print("Enter the correct menu")
            exit()


user_response()
