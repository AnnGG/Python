import json
import sqlite3
import requests
from collections import Counter


class BankException(object):
    pass


class NegativeMeaning(object):
    pass


def connect_db():
    conn = None
    try:
        conn = sqlite3.connect("atm.db")
    except sqlite3.Error as e:
        print(e)
    return conn


def elements_counter(some_list):
    counter = Counter()
    for element in some_list:
        counter[element] += 1
    return counter.most_common()


def create_user_table(database):
    cur = database.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
               (login TEXT NOT NULL PRIMARY KEY,
               password TEXT NOT NULL,
               collector BOOLEAN NOT NULL CHECK (collector IN (0,1)))''')
    cur.execute('''SELECT * FROM users''')

    if cur.fetchall() is None:
        users = [('user1', 'user1', 0),
                 ('user2', 'user2', 0),
                 ('admin', 'admin', 1)]

        cur.executemany("INSERT INTO users VALUES (?,?,?)", users)
        database.commit()


def create_balance_table(database):
    cur = database.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS balance
               (user_login TEXT PRIMARY KEY REFERENCES users(login),
               user_balance INTEGER) ''')

    cur.execute('''SELECT * FROM balance''')

    if cur.fetchall() is None:
        balance = [
            ('user1', 1000),
            ('user2', 7000),
            ('admin', 0)]

        cur.executemany("INSERT INTO balance VALUES (?,?)", balance)
        database.commit()



def create_denomination_table(database):
    cur = database.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS denominations
               (denom_name INTEGER NOT NULL PRIMARY KEY,
               denom_balance INTEGER NOT NULL) ''')

    cur.execute('''SELECT * FROM denominations''')

    if cur.fetchall() is None:
        denominations = [
            (10, 1),
            (20, 10),
            (50, 10),
            (100, 10),
            (200, 10),
            (500, 10),
            (1000, 10)]

        cur.executemany("INSERT INTO denominations VALUES (?,?)", denominations)
        database.commit()


def create_transaction_table(database):
    cur = database.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions
               (id_transact INTEGER PRIMARY KEY AUTOINCREMENT,
               user_login TEXT REFERENCES users(login),
               transaction_name TEXT,
               transaction_information TEXT) ''')

    database.commit()


def check_users():
    database = connect_db()
    cur = database.cursor()
    cur.execute('''SELECT * FROM users''')
    fetched = cur.fetchall()
    database.close()
    return fetched


def login_password(users):
    username = input("Input user name: ")
    password = input("Input parol: ")
    for user in users:
        if len(user) == 3 and user[0] == username and user[1] == password and user[2] == 1:
            return username, True, True
        elif user[0] == username and user[1] == password:
            return username, True, False

    return username, False, False


def register_user(user_name, password, is_admin=None):
    database = connect_db()
    cur = database.cursor()
    user = (user_name, password, is_admin)
    cur.execute("INSERT INTO users VALUES (?,?,?)", user)
    database.commit()
    cur.execute("INSERT INTO balance VALUES (?,?)", (user_name, 0))
    database.commit()
    return cur.lastrowid


def check_correct_summ(summ):
    for i in summ:
        if i.isalpha():
            summ = input('Enter right sum, without symbols: ')
            break
    summ = abs(int(summ))
    return summ


def check_atm_denominations():
    database = connect_db()
    cur = database.cursor()
    cur.execute('SELECT * FROM denominations')
    rows = cur.fetchall()
    return rows


def add_denomination_cash(denom):
    database = connect_db()
    cur = database.cursor()
    list_denom = check_atm_denominations()
    dict_denom = {i[0]: i[1] for i in list_denom}
    result_list = []
    for i in dict_denom:
        if i not in denom:
            continue
        new_value = dict_denom.get(i)
        new_value = int(new_value) + int(denom.get(i))
        dict_denom.update({i: new_value})
    for i in dict_denom:
        result_list.append((dict_denom.get(i), i))
    cur.executemany('''UPDATE denominations SET denom_balance = ?
                    WHERE denom_name = ? ''', result_list)
    database.commit()


def menu_collector():
    while True:

        print(' 1 - Check availability of bills ATM'
              '\n 2 - Top up the number of bills ATM'
              '\n 3 - Exit')

        user_option = input('Select an option: ')

        if user_option == '1':
            print("-" * 40)
            print(check_atm_denominations())

        elif user_option == '2':
            denom_list = [10, 20, 50, 100, 200, 500, 1000]
            input_denom = input(f'Enter denomination {denom_list} : ')
            input_denom = check_correct_summ(input_denom)
            if input_denom in denom_list:
                count_denom = input('Enter count for this denomination: ')
                count_denom = check_correct_summ(count_denom)
                denom_dict = {input_denom: count_denom}
                add_denomination_cash(denom_dict)
                print('Successful')
            else:
                print('Incorrect denomination')

        elif user_option == '3':
            print('Exit')
            exit()
        else:

            print('Enter correct option')

            break


def check_user_balance(user_name):
    database = connect_db()
    cur = database.cursor()
    cur.execute('SELECT * from balance')
    rows = cur.fetchall()
    for i in rows:
        if i[0] == user_name:
            return i[1]
        if i[1] is None:
            i[0] = 0
    return False


def users_transactions(user_name, type_transact, output):
    database = connect_db()
    cur = database.cursor()
    cur.execute('''INSERT INTO transactions(user_login,transaction_name,transaction_information)
                   VALUES (?,?,?) ''', (user_name, type_transact, output))
    database.commit()


def change_balance(user, summ):
    database = connect_db()
    cur = database.cursor()
    balance = check_user_balance(user)
    result = balance + summ
    if result < 0 or result == False:
        print('A little money on the card')
        return False
    else:
        cur.execute('''UPDATE balance SET user_balance = ?
                    WHERE user_login = ? ''', (result, user))
        database.commit()
        return True


def current_exchange_rate():
    response_API = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = response_API.text
    parse_json = json.loads(data)
    parse_json1 = parse_json[0:-1]
    parse_json2 = parse_json[-1]
    list_parse_json2 = list(parse_json2.values())

    for i in parse_json1:
        data_exchange = list(i.values())

        print(data_exchange[0], " " * 8, data_exchange[1])
        print(round(float(data_exchange[2]), 2), " " * 7, round(float(data_exchange[3]), 2))
        print("-" * 20)

    print(list_parse_json2[0], " " * 8, list_parse_json2[1])
    print(round(float(list_parse_json2[2]), 1), " " * 4, round(float(list_parse_json2[3]), 2))


def change(new_values: dict):
    database = connect_db()
    cur = database.cursor()
    for value in new_values:
        cur.execute(f"UPDATE denominations SET denom_balance = '{new_values[value]}' WHERE denom_name = '{value}'")
    database.commit()


def withdraw_balance(user):
    database = connect_db()
    cur = database.cursor()
    atm = cur.execute("SELECT * FROM denominations").fetchall()
    money_in = {bank[0]: bank[1] for bank in atm}
    summ_in = 0
    for denomination in money_in:
        if int(money_in[denomination]) != 0:
            print(f'{denomination}', end=' ')
            summ_in += int(money_in[denomination]) * int(denomination)
    summ = int(input('\nInput the amount you want to withdraw  '))
    if summ <= 0:
        raise NegativeMeaning()
    if summ_in < summ:
        print(f'ATM doesn`t have enough money')
        if input('do you want to continue (print yes or no)') == 'yes':
            menu_user(user)
        else:
            exit()

    old_balance = cur.execute(f"SELECT * FROM balance WHERE user_login='{user}'").fetchone()
    if summ > old_balance[1]:
        print(f'You don`t have enough money on the balance')
        if input('do you want to continue (print yes or no)') == 'yes':
            menu_user(user)
        else:
            exit()
    denominations_give = []
    money_after_give = money_in.copy()
    summ_to_give = summ
    iterlist = list(money_in.keys())
    iterlist.sort(key=lambda x: int(x), reverse=True)
    while summ_to_give > 0:
        for denomination in iterlist:
            if int(money_after_give[denomination]) != 0 and summ_to_give % int(denomination) == 0:
                summ_to_give -= int(denomination)
                denominations_give.append(int(denomination))
                money_after_give[denomination] -= 1
            else:
                continue
            break
        else:
            print('ATM can`t give you that summ')

    change_balance(user, -summ)
    new_balance = check_user_balance(user)
    users_transactions(user, 'withdrow', new_balance)
    print(f'You received')
    for element in elements_counter(denominations_give):
        print(f'{element[0]} - {element[1]} bills')

    change(money_after_give)
    if input('do ypu want to continue (print yes or no) ') == 'yes':
        menu_user(user)
    else:
        exit()


def menu_user(user):
    while True:
        print(' 1 - Check the balance'
              '\n 2 - Top up your balance'
              '\n 3 - Take money'
              '\n 4 - Current exchange rate'
              '\n 5 - Exit')

        user_option = input('Select an option: ')

        if user_option == '1':
            type_transact = 'Check the balance'
            output = check_user_balance(user)
            users_transactions(user, type_transact, output)
            print(f'You have {output} money')

        elif user_option == '2':
            summ = input('How much do you want to top up? ')
            result = check_correct_summ(summ)
            change_balance(user, result)
            print('You have toped up your balance')
            type_transact = 'Top up the balance'
            users_transactions(user, type_transact, result)
        elif user_option == '3':
            withdraw_balance(user)
        elif user_option == '4':
            print('Current exchange rate\n')
            current_exchange_rate()

        elif user_option == '5':
            print('Exit')
            exit()
        else:
            print('Enter correct option')
            break


def start():
    database = connect_db()
    if database is not None:
        create_user_table(database)
        create_balance_table(database)
        create_denomination_table(database)
        create_transaction_table(database)

    users = check_users()
    username, password, collector = login_password(users)

    if password == False and collector == False:
        print('You entered incorrect login or password')
        new_user = input('Do you want to register? (yes/no): ')

        if new_user == 'yes':
            new_user_login = input('Enter login: ')
            new_user_password = input('Enter password: ')
            user_is_admin = input('Are you incasator? (yes/no): ')

            if user_is_admin == 'yes':
                user_is_admin = 1
                register_user(new_user_login, new_user_password, user_is_admin)

            elif user_is_admin == 'no':
                user_is_admin = 0
                register_user(new_user_login, new_user_password, user_is_admin)

            else:
                print('You input incorrect symbols')

        elif new_user == 'no':
            print('EXIT')
        else:
            print('You input incorrect symbols')

    elif password == True and collector == True:
        menu_collector()

    elif password == True and collector == False:
        menu_user(username)

    else:
        ("Unknown operation")

start()