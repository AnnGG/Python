# Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
# які зберігатиме в відповідні змінні.
# Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.


class Person(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    def print_name(self):
        print("My name is:", self.name)

    def show_age(self):
        print("I am", self.age, " years old.")

    def show_all_information(self):
        for key, value in self.__dict__.items():
            print(key, "=", value)


person1 = Person(name="Piter", age=37)
person2 = Person(name="Lion", age=39)

person1.print_name()
person1.show_age()
person1.profession = "doctor"
person1.show_all_information()

print('-'*40)

person2.print_name()
person2.show_age()
person2.profession = "engineer"
person2.show_all_information()
