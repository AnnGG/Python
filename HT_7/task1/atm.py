#Програма-банкомат.
#Створити програму з наступним функціоналом:
#- підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#- кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#- є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#Особливості реалізації:
#- файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#- файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#- файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#Особливості функціонала:
#- за кожен функціонал відповідає окрема функція;
#- основна функція - <start()> - буде в собі містити весь workflow банкомата:
#- спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#- потім - елементарне меню типа:
#Введіть дію:
#1. Продивитись баланс
#2. Поповнити баланс
#3. Зняти гроші
#4. Вихід
#- далі - фантазія і креатив :)


import json

import datetime

class LoginException(Exception):

          pass


def check_balance(person):

    if person == "Ivan":

        with open("ivan_balance.txt", "r") as f:

            balance = f.read()

    elif person == "KL":

        with open("kl_balance.txt", "r") as f:

            balance = f.read()

    elif person == "Olga":

        with open("olga_balance.txt", "r") as f:

            balance = f.read()
    
    return(balance)

                
def withdraw_money(person, money):

    if round(float(check_balance(person)),2) - money >= 0:

        now = datetime.datetime.now()

        now_t = now.strftime("%d-%m-%Y %H:%M")

        user_money = round(float(check_balance(person)),2) - money

        print('You have withdrawn {} grn.'.format(money))

        print('---------------------\n')

        if person == "Ivan":

            with open("ivan_balance.txt", "w") as f:

                f.write(str(user_money))

            filename = 'ivan.json'

            with open(filename, 'a') as f_obj:

                f_obj.write('\n')

                json.dump({"action":"withdrawn","sum":money,"currency":"grn", "data":now_t}, f_obj) 

        elif person == "KL":

            with open("kl_balance.txt", "w") as f:

                f.write(str(user_money))

            filename = 'kl.json'

            with open(filename, 'a') as f_obj:

                f_obj.write('\n')

                json.dump({"action":"withdrawn","sum":money,"currency":"grn", "data":now_t}, f_obj)

        elif person == "Olga":

            with open("olga_balance.txt", "w") as f:

                f.write(str(user_money))

            filename = 'olga.json'

            with open(filename, 'a') as f_obj:

                f_obj.write('\n')

                json.dump({"action":"withdrawn","sum":money,"currency":"grn", "data":now_t}, f_obj)
            
    else:

        print("There is not enough money in your account!")

        print('---------------------\n')


def top_up_balance(person, money):

    now = datetime.datetime.now()

    now_t = now.strftime("%d-%m-%Y %H:%M")

    user_money = round(float(check_balance(person)),2) + money

    print('You have topped up your balance to {} grn.'.format(money))

    print('---------------------\n')

    if person == "Ivan":

        with open("ivan_balance.txt", "w") as f:

            f.write(str(user_money))

        filename = 'ivan.json'

        with open(filename, 'a') as f_obj:

            f_obj.write('\n')

            json.dump({"action":"replenishment","sum":money,"currency":"grn", "data":now_t}, f_obj)

    elif person == "KL":

        with open("kl_balance.txt", "w") as f:

            f.write(str(user_money))

        filename = 'kl.json'

        with open(filename, 'a') as f_obj:

            f_obj.write('\n')

            json.dump({"action":"replenishment","sum":money,"currency":"grn", "data":now_t}, f_obj)

    elif person == "Olga":

        with open("olga_balance.txt", "w") as f:

            f.write(str(user_money))

        filename = 'olga.json'

        with open(filename, 'a') as f_obj:

            f_obj.write('\n')

            json.dump({"action":"replenishment","sum":money,"currency":"grn", "data":now_t}, f_obj)

def login_password(username, password ):

    credentials = {}

    with open("users.txt", "r") as f:

        for line in f:

            user, pwd = line.strip().split(':')

            credentials[user] = pwd

        try:

            if username in credentials and password == credentials[username]:

                return True

            else:

                raise LoginException("Ops")

        except LoginException:

            print("Ops LoginException")   

            exit()

def start():

    print("Input your username")

    username = input()

    print("Input your password")

    password = input()

    print("----Login Status----")

    if (login_password(username, password )) == True:

        print("Welcome to the ATM system.")

        print('---------------------\n')

        while True:

            choice = int(input('Select item:\n'
                               '1. Check balance\n'
                               '2. Withdraw money\n'
                               '3. Top up balance\n'
                               '4. Exit\n '
                               '---------------------\n'
                               'Your choice:'))
            if choice == int(4):

                print('Good buy!')

                break

            elif choice == int(1):

                print("On your account")

                print(check_balance(username), " grn")

                print('---------------------\n')

            elif choice == int(2):

                money = float(input("How much do you want to withdraw? "))

                withdraw_money(username, money)

            elif choice == int(3):

                money = float(input("How much do you want to deposit? "))

                top_up_balance(username, money) 
                
start()




