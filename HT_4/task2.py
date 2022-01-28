# Написати функцію < bank > , яка працює за наступною логікою:
# користувач робить вклад у розмірі < a > одиниць строком на < years > років
# під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).#
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.

from math import *

def bank(user_deposit, user_years, user_percent = 10):

    user_total = user_deposit * pow((1 + 10/100),user_years)

    return(round(user_total,2))

user_deposit = float(input("Enter the amount of your deposit. For example 102.2: "))

user_years = int(input("Specify the term of the deposit: "))

print("After the expiration of the term of the deposit, your account will be")

print(bank(user_deposit, user_years))

    
