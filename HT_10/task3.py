#Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
#Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
#конвертацію введеної суми з однієї валюти в іншу.

import requests
import json
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def response_api_pr(url_api):

    day_now = datetime.now()

    date_api = day_now.strftime('%d.%m.%Y')

    api_param = {"date": date_api}

    response_api = requests.get(url_api, api_param)

    data_api = response_api.text

    parse_json_api = json.loads(data_api)

    data_parse_json_api = {}

    for data in parse_json_api['exchangeRate']:

        data_parse_json_api[data.get('currency')] = [data.get('saleRateNB'), data.get('purchaseRateNB')]

    return data_parse_json_api


user_url_api = 'https://api.privatbank.ua/p24api/exchange_rates?json'

data_currency_exchange = response_api_pr(user_url_api)

print("\nToday the following currencies are bought and sold")

print("-" * 40)

print(" " * 6, "Purchase", " " * 6, "Sale")

print("-" * 40)

for currency, rate_currency in data_currency_exchange.items():

    if currency is not None:

        round_purchase = Decimal(str(rate_currency[0]))

        purchase = round_purchase.quantize(Decimal('0.01'), ROUND_HALF_UP)

        round_sale = Decimal(str(rate_currency[1]))

        sale = round_sale.quantize(Decimal('0.01'), ROUND_HALF_UP)

        print(currency, "  ", purchase, "  " * 4, sale)

print("-" * 40)

currency_sale = input("Enter the currency you want to sell: ")

currency_purchase = input("Enter the currency you want to buy: ")

user_amount_money = float(input("Enter the amount: "))

print("-" * 40)

if user_amount_money > 0:

    if currency_sale in response_api_pr(user_url_api).keys():

        if currency_purchase in response_api_pr(user_url_api).keys():

            if currency_sale == "UAN":

                exchange = Decimal(str(user_amount_money / (data_currency_exchange[currency_purchase][1])))

                print(exchange.quantize(Decimal('0.01'), ROUND_HALF_UP))

            else:

                exchange = (data_currency_exchange[currency_sale][0]) * user_amount_money

                exchange1 = Decimal(str(exchange / (data_currency_exchange[currency_purchase][1])))

                print(exchange1.quantize(Decimal('0.01'), ROUND_HALF_UP))

        else:

            print("There is no such currency!")
    else:

        print("There is no such currency!")
else:

    print("The amount cannot be negative!")
