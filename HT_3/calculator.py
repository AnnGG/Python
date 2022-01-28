# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя
# яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(number1, operator, number2):

    if operator in ('+', '-', '*', '/'):

        print("The result of your expression")

        if operator == '+':

            return float(number1) + float(number2)

        elif operator == '-':

            return float(number1) - float(number2)

        elif operator == '*':

            return float(number1) * float(number2)

        elif operator == '/':

            if number2!= 0:

                return float(number1) / float(number2)

            else:

                print("Division by zero !")   
    else:

        print("This operation cannot be performed!")

print("Enter your expression on one line")

number1, operator, number2 = input().split()

print(calculator(number1, operator, number2))
        
