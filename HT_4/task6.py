# Вводиться число. Якщо це число додатне, знайти його квадрат,
# якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

def change_number(number):

    if number > 0:

        return number * number

    elif number < 0:

        return number + 100

    elif number == 0:

        return(number)

number = float(input("Input number: "))

print(change_number(number))
