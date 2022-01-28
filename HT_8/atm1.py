#Доповніть програму-банкомат з попереднього завдання таким функціоналом,
#як використання банкнот.
#Отже, у банкомата повинен бути такий режим як "інкассація",
#за допомогою якого в нього можна "загрузити" деяку кількість банкнот
#(вибирається номінал і кількість).
#Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
#Особливості реалізації:
#- перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#- у одного користувача повинні бути права "інкасатора".
#Відповідно і у нього буде своє власне меню із пунктами:
#- переглянути наявні купюри;
#- змінити кількість купюр;
#- видача грошей для користувачів відбувається в межах наявних купюр;
#- якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат -
#не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить,
#відкладає в окрему касету.
#Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для
#старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
#До того ж, скоріш за все, вам прийдеться і так багато чого переписати.

import json

import datetime

class LoginException(Exception):

          pass


def login_password(username, password, encoding='utf-8'):

    with open("users.txt", "r") as f:

        user_list = []

        users = f.read().split('\n')

        for i in range(len(users)):

            user = users[i].split(', ')

            user_list.append(user)

        for user in user_list:

            if len(user) == 3 and user[0] == username and user[1] == password and user[2] == 'True':

                return True, True

            elif user[0] == username and user[1] == password:

                return True, False

        return False, False


def user_check_balance(person):

    with open(f'{person}_balance.txt', 'r', encoding='utf-8') as balance:

        balance_user = balance.readline()

        return(balance_user)

def user_withdraw_money(person, money):

    if money > 0:

        with open(f'{person}_balance.txt', 'r', encoding='utf-8') as balance:

            balance_user = balance.readline()

            if int(balance_user) - money >=0:

                with open('inc_money.txt', 'r', encoding='utf-8') as inc_money:

                    inc_money_f = inc_money.readline()

                    inc_money_f = json.loads(inc_money_f)

                    print('The following denominations are available:')

                    for denomination in inc_money_f:

                        if int(inc_money_f[denomination])!= 0:

                            print(f'{denomination}', end=' ')

                    
                    balance_money_atm = []

                    balance_after_give = inc_money_f.copy()

                    give_user_sum = money

                    money_atm_list = list(inc_money_f.keys())

                    money_atm_list.sort(key=lambda x: int(x), reverse=True)

                    while give_user_sum > 0:

                        for denomination in money_atm_list:

                            if int(balance_after_give[denomination]) != 0 and give_user_sum % int(denomination) == 0:

                                give_user_sum -= int(denomination)

                                balance_money_atm.append(int(denomination))

                                balance_after_give[denomination] -= 1

                            else:

                                continue
                            break

                        else:

                            print('\nATM can`t give you that money!')

                            if input('Do you want to continue (print yes or no) ') == 'yes':

                                user_menu(person)

                            else:

                                print('Good buy!')

                                exit()
                                
                                break

                    user_money = int(balance_user) - money

                    print('\nYou have withdrawn {} grn.'.format(money))

                    balance_money_atm_d = {}

                    for money_atm in balance_money_atm:

                        if money_atm in balance_money_atm_d:

                            balance_money_atm_d[money_atm]+= 1

                        else:

                            balance_money_atm_d[money_atm] = 1

                    for nominal, units in balance_money_atm_d.items():

                        print(nominal, " - ", units, " units ")
                            
                    print('---------------------\n')

                with open(f'{person}_balance.txt', 'w', encoding='utf-8') as balance:

                    balance.write(str(user_money))

                with open(f'{person}.json', 'a', encoding='utf-8') as f_obj:

                    now = datetime.datetime.now()

                    now_t = now.strftime("%d-%m-%Y %H:%M")

                    f_obj.write('\n')

                    json.dump({"action":"withdrawn","sum":money,"currency":"grn", "data":now_t}, f_obj)

                with open('inc_money.txt', 'w', encoding='utf-8') as inc_money:

                    balance_after_give = json.dumps(balance_after_give)

                    inc_money.write(balance_after_give)
            else:

                print("There is not enough money in your account!")

                print('---------------------\n')
    else:

        print("The amount cannot be negative!")

        print('---------------------\n')

                
def user_top_up_balance(person, money):

    if money >= 0:

        now = datetime.datetime.now()

        now_t = now.strftime("%d-%m-%Y %H:%M")

        with open(f'{person}_balance.txt', 'r', encoding='utf-8') as balance:

            balance_user = balance.readline()

            user_money = int(balance_user) + money

            print('You have topped up your balance to {} grn.'.format(int(money)))

            print('---------------------\n')

        with open(f'{person}_balance.txt', 'w', encoding='utf-8') as balance:

            balance.write(str(int(user_money)))

        with open(f'{person}.json', 'a', encoding='utf-8') as f_obj:

            f_obj.write('\n')

            json.dump({"action":"withdrawn","sum":money,"currency":"grn", "data":now_t}, f_obj) 

    else:

        print("The amount cannot be negative!")

        print('---------------------\n')


def incasator_checking_money(incasator):

    with open('inc_money.txt', 'r', encoding='utf-8') as inc_money:

        inc_money = inc_money.readline()

        inc_money = json.loads(inc_money)

        for denomination in inc_money:

            print(f'{denomination}: {inc_money[denomination]}')


def incasator_top_up_denominations(incasator):

    with open('inc_money.txt', 'r', encoding='utf-8') as inc_money:

        inc_money = inc_money.readline()

        inc_money = json.loads(inc_money)

        for denomination in inc_money:

            numbers = int(input(f'Input count denomination {denomination}: '))

            if numbers <= 0:

                print("You can`t add negative count of money!")

            inc_money[denomination] += numbers

    with open('inc_money.txt', 'w', encoding='utf-8') as inc_load_money:

        inc_money = json.dumps(inc_money)

        inc_load_money.write(inc_money)

        print('You have successfully loaded the required denominations!')


def user_menu(username):

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

                print(user_check_balance(username), " grn")

                print('---------------------\n')

            elif choice == int(2):

                money = int(input("How much do you want to withdraw? "))

                user_withdraw_money(username, money)

            elif choice == int(3):

                money = float(input("How much do you want to deposit? "))

                user_top_up_balance(username, money)

            else:

                print("This item is not on the menu!")

                print('---------------------\n')

    
def incasator_menu(username):

    while True:

            choice = int(input('Select item:\n'
                               '1. Check balance\n'
                               '2. Top up balance\n'
                               '3. Exit\n '
                               '---------------------\n'
                               'Your choice:'))
            if choice == int(3):

                print('Good buy!')

                break

            elif choice == int(1):

                print("The following banknotes are now in stock:")

                incasator_checking_money(username)

                print('---------------------\n')

            elif choice == int(2):

                print(incasator_top_up_denominations(username))             

                print('---------------------\n')

def start():

    print("Input your username")

    username = input()

    print("Input your password")

    password = input()

    login_result, collector = login_password(username, password)

    print("----Login Status----")

    try:
        if login_password(username, password ) == (True, False):

            print("Welcome to the user menu ATM system.")

            print('---------------------\n')

            
            user_menu(username)

        elif login_password(username, password ) == (True, True):

            print("Welcome to the incasator menu ATM system.")

            print('---------------------\n')
          
            incasator_menu(username)

        else:

            raise LoginException("Ops")

    except LoginException:

            print("Ops LoginException")

            exit()
        
start()





