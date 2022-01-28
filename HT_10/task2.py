# Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
# - Перелік валют краще принтануть.
#  - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
# - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
# - Також перевірте, чи введена правильна валюта.
# Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
# курсу обраної валюти (Нацбанк) від введеної дати до поточної.

from datetime import datetime, timedelta
import requests
import json

print("Select currency")
print('\nAZN BYN CAD CHF CNY CZK DKK EUR GBP GEL HUF ILS JPY KZT MDL NOK PLN RUB SEK SGD TMT TRY UAH USD UZS')

try:
    user_day = input("Input your data %d.%m.%Y: ")
    check_user_date = datetime.strptime(user_day, "%d.%m.%Y")
    day_today = datetime.today().strftime('%d.%m.%Y')
    current_datetime1 = datetime.strptime(day_today, "%d.%m.%Y")
    if check_user_date <= current_datetime1:
        user_currency = input("Enter currency: ")
        if user_currency.isalpha():
            if user_currency in ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF',
                                 'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'RUB', 'SEK', 'SGD', 'TMT', 'TRY',
                                 'UAH', 'USD', 'UZS']:

                someday = user_day.split('.')
                str_day_today = day_today
                str_day_today = str_day_today.split('.')
                diff = int(str_day_today[0]) - int(someday[0])
                data_api = {}

                for days_i in range(0, abs(diff) + 1):
                    next_day = datetime.strptime(user_day, '%d.%m.%Y') + timedelta(days=days_i)
                    next_day_modif = next_day.strftime('%d.%m.%Y')
                    api_param = {"date": next_day_modif}
                    data_api_pr = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json', api_param)
                    data_api_pr_modif = data_api_pr.text
                    parse_json = json.loads(data_api_pr_modif)

                    for data_exchange in parse_json['exchangeRate']:
                        if data_exchange.get('currency') == user_currency:
                            purchase_currency = data_exchange.get('purchaseRateNB')
                            data_api[parse_json['date']] = purchase_currency

                list_date = list(data_api.keys())
                list_purchase_currency = list(data_api.values())

                diff_list = []

                for i_list_purchase_currency in range(1, len(list_purchase_currency)):
                    diff_list.append(
                        (list_purchase_currency[i_list_purchase_currency] - list_purchase_currency[
                            i_list_purchase_currency - 1]))
                print("Currency: ", user_currency)
                print("Date: ", list_date[0])
                print("NBU:  ", list_purchase_currency[0], " " * 10, "-" * 10)

                for i_day_currency, i_list_purchase_currency, diff_list in zip(list_date[1:],
                                                                               list_purchase_currency[1:],
                                                                               diff_list):
                    print("Date: ", i_day_currency)
                    print("NBU:  ", i_list_purchase_currency, " " * 10, diff_list)
            else:
                print("Please enter the correct currency!")
        else:
            print("Please enter the correct currency!")

    else:
        print("Please enter the correct date!")

except ValueError:
    print('The date {} is invalid'.format(user_day))
