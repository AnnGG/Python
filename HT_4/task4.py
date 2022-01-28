# Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона

import math

def prime_list(number1, number2):

    prime_list = []
    
    for number in range(number1, number2 + 1):

        if number == 0 or number == 1:

            continue

        for i_number in range(2, int(math.sqrt(number)) + 1):

            if number % i_number == 0:

                break 

        else:

            prime_list.append(number)


    return(prime_list)
    

number1 = int(input("Input number 1: "))

number2 = int(input("Input number 2: "))

print("Your list of prime numbers")

print(prime_list(number1, number2))
