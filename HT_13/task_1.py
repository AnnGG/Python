# Створити клас Calc, який буде мати атребут last_result та 4 методи.
# Методи повинні виконувати математичні операції з 2-ма числами,
# а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result
# він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result
# повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас


class Calc(object):
    '''The class Calc is used to evaluate two variables'''

    last_result = None

    def add_number(self, first_number, second_number):
        '''Method for finding the sum of the numbers'''

        self.last_result = first_number + second_number

    def sub_number(self, first_number, second_number):
        '''Method for finding the difference of the numbers'''

        self.last_result = first_number - second_number

    def mult_number(self, first_number, second_number):
        '''Method for finding the multiplication of the numbers'''

        self.last_result = first_number * second_number

    def div_number(self, first_number, second_number):
        '''Method for finding the division of the numbers'''
        
        try:
            self.last_result = first_number / second_number
        except ZeroDivisionError:
            return "You cannot divide by zero!"


calculator1 = Calc()
calculator1.add_number(2, 2)
print(calculator1.last_result)
