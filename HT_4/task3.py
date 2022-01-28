# Написати функцию < is_prime >, яка прийматиме 1 аргумент
# - число від 0 до 1000, и яка вертатиме True,
# якщо це число просте, и False - якщо ні.

import math

def is_prime(number):

    if 0 <= number <= 1000:

        if number <= 1:

            return "False"

        for i_number in range(2, int(math.sqrt(number)) + 1):

            if number % i_number == 0:

                return "False"

        return "True"

    else:

        return("The number is not in this range")

user_number = int(input("Input number: "))

print(is_prime(user_number))
