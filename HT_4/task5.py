#Написати функцію < fibonacci >, яка приймає один аргумент
#і виводить всі числа Фібоначчі,що не перевищують його.

def fibonacci(user_number):

    if user_number == 0:

        print(user_number)

    else:

        fib1,fib2 = 0,1

        while fib1 <= user_number:

            print(fib1, end=" ")

            fib1,fib2 = fib2, fib1 + fib2


print("Enter the number for which you want to form a Fibonacci series")

fibonacci(int(input()))
