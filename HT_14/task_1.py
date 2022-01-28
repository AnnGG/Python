import sqlite3
import json
import requests
from collections import Counter



class NegativeNumber(Exception):
    pass


class DatabaseConnection(object):

    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


class Authorization(object):

    def check_users(self):

        with DatabaseConnection('atm.db') as connection:

            cur = connection.cursor()
            cur.execute('''SELECT * FROM users''')
            fetched = cur.fetchall()
            return fetched

    def login_password(self, users):

        username = input("Input user name: ")
        password = input("Input parol: ")
        for user in users:
            if len(user) == 3 and user[0] == username and user[1] == password and user[2] == 1:
                return username, True, True
            elif user[0] == username and user[1] == password:
                return username, True, False

        return username, False, False


class Atm(object):

    def check_correct_summ(self, summ):

        for i in summ:
            if i.isalpha():
                summ = input('Enter right sum, without symbols!')
                exit()
        summ = abs(int(summ))
        return summ

    def elements_counter(self, some_list):

        counter = Counter()
        for element in some_list:
            counter[element] += 1
        return counter.most_common()

    def change_denom(self, new_values: dict):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            for value in new_values:
                cur.execute(
                    f"UPDATE denominations SET denom_balance = '{new_values[value]}' WHERE denom_name = '{value}'")

    def register_user(self, user_name, password, is_admin=None):
        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            user = (user_name, password, is_admin)
            cur.execute("INSERT INTO users VALUES (?,?,?)", user)
            cur.execute("INSERT INTO balance VALUES (?,?)", (user_name, 0))
            return cur.lastrowid

    def users_transactions(self, user_name, type_transact, output):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            cur.execute('''INSERT INTO transactions(user_login,transaction_name,transaction_information)
                       VALUES (?,?,?) ''', (user_name, type_transact, output))

    def check_user_balance(self, user_name):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            cur.execute('SELECT * from balance')
            rows = cur.fetchall()
            for i in rows:
                if i[0] == user_name:
                    return i[1]
                if i[1] is None:
                    i[0] = 0
            return False

    def change_user_balance(self, user_log, user_summ):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            balance = self.check_user_balance(user_log)
            result = balance + user_summ
            if result < 0 or result == False:
                print('A little money on the card')
                return False
            else:
                cur.execute('''UPDATE balance SET user_balance = ?
                            WHERE user_login = ? ''', (result, user_log))
                return True

    def give_money_user(self, user_log):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            atm = cur.execute("SELECT * FROM denominations").fetchall()
            money_in = {bank[0]: bank[1] for bank in atm}
            summ_in = 0
            print("The following denominations are available")
            for denomination in money_in:
                if int(money_in[denomination]) != 0:
                    print(f'{denomination}', end=' ')
                    summ_in += int(money_in[denomination]) * int(denomination)
            summ = user.withdraw_money()
            if summ <= 0:
                raise NegativeNumber()
            if summ_in < summ:
                print(f'ATM doesn`t have enough money')
                if input('Do you want to continue (print yes or no)') == 'yes':
                    menu.menu_user(user_log)
                else:
                    exit()

            old_balance = cur.execute(f"SELECT * FROM balance WHERE user_login='{user_log}'").fetchone()
            if summ > old_balance[1]:
                print(f'You don`t have enough money on the balance')
                if input('Do you want to continue (print yes or no)') == 'yes':
                    menu.menu_user(user_log)
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
                    if input('Do you want to continue (print yes or no)') == 'yes':
                        menu.menu_user(user_log)
                    else:
                        exit()

            self.change_user_balance(user_log, -summ)
            new_balance = self.check_user_balance(user_log)
            self.users_transactions(user_log, 'withdrow', new_balance)
            print(f'You received')
            for element in self.elements_counter(denominations_give):
                print(f'{element[0]} - {element[1]} bills')

            self.change_denom(money_after_give)
            if input('Do you want to continue (print yes or no) ') == 'yes':
                menu.menu_user(user_log)
            else:
                exit()

    def check_atm_denominations(self):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            cur.execute('SELECT * FROM denominations')
            rows = cur.fetchall()
            return rows

    def add_denomination_cash(self, denom):

        with DatabaseConnection('atm.db') as connection:
            cur = connection.cursor()
            list_denom = self.check_atm_denominations()
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


class Person(object):

    def registration(self):

        new_user = input('Do you want to register? (yes/no): ')

        if new_user == 'yes':
            new_user_login = input('Enter login: ')
            new_user_password = input('Enter password: ')
            user_is_admin = input('Are you incasator? (yes/no): ')

            if user_is_admin == 'yes':
                user_is_admin = 1
                atm.register_user(new_user_login, new_user_password, user_is_admin)
                menu.menu_collector()

            elif user_is_admin == 'no':
                user_is_admin = 0
                atm.register_user(new_user_login, new_user_password, user_is_admin)
                menu.menu_user(new_user_login)

            else:
                print('You input incorrect symbols')

        elif new_user == 'no':
            print('EXIT')
        else:
            print('You input incorrect symbols')

    def current_exchange_rate(self):

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
        print("-" * 20)


class Incasator(Person):

    def add_cash_to_atm(self):

        denom_list = [10, 20, 50, 100, 200, 500, 1000]
        input_denom = input(f'Enter denomination {denom_list} : ')
        input_denom = atm.check_correct_summ(input_denom)
        if input_denom in denom_list:
            count_denom = input('Enter count for this denomination: ')
            count_denom = atm.check_correct_summ(count_denom)
            denom_dict = {input_denom: count_denom}
            print('Successful')
            return (denom_dict)
        else:
            print('Incorrect denomination')


class User(Person):

    def top_up_balance(self):

        summ = input('How much do you want to top up? ')
        result = atm.check_correct_summ(summ)
        print(f'You have toped up your balance on ${result}')
        return result

    def withdraw_money(self):

        sum_user = int(input('\nInput the amount you want to withdraw:  '))
        return sum_user


class Menu(object):

    def menu_collector(self):

        while True:
            print('=' * 10, 'Welcome to the ATM system', '=' * 10)
            print('\n 1 - Check availability of bills ATM'
                  '\n 2 - Top up the number of bills ATM'
                  '\n 3 - Current exchange rate'
                  '\n 4 - Exit')

            user_option = input('Select an option: ')

            if user_option == '1':
                print("-" * 40)
                print(atm.check_atm_denominations())

            elif user_option == '2':
                atm.add_denomination_cash(incasator.add_cash_to_atm())

            elif user_option == '3':
                incasator.current_exchange_rate()

            elif user_option == '4':
                print('Exit')
                exit()
            else:
                print('Enter correct option')
                break

    def menu_user(self, customer):

        while True:
            print('=' * 10, 'Welcome to the ATM system', '=' * 10)
            print('\n 1 - Check the balance'
                  '\n 2 - Top up your balance'
                  '\n 3 - Withdraw money'
                  '\n 4 - Current exchange rate'
                  '\n 5 - Exit')

            user_option = input('Select an option: ')

            if user_option == '1':
                type_transact = 'Check the balance'
                output = atm.check_user_balance(customer)
                atm.users_transactions(customer, type_transact, output)
                print(f'You have {output} money')

            elif user_option == '2':
                top_up = user.top_up_balance()
                atm.change_user_balance(customer, top_up)
                atm.check_user_balance(customer)
                type_transact = 'Top up the balance'
                atm.users_transactions(customer, type_transact, top_up)

            elif user_option == '3':
                atm.give_money_user(customer)

            elif user_option == '4':
                print('Current exchange rate\n')
                user.current_exchange_rate()

            elif user_option == '5':
                print('Exit')
                exit()
            else:
                print('Enter correct option')
                break


login = Authorization()
atm = Atm()
person = Person()
incasator = Incasator()
user = User()
menu = Menu()


def main():

    users = login.check_users()
    username, password, collector = login.login_password(users)

    if password == False and collector == False:
        print('You entered incorrect login or password')
        person.registration()

    elif password == True and collector == True:
        menu.menu_collector()

    elif password == True and collector == False:
        menu.menu_user(username)

    else:
        ("Unknown operation")


main()
