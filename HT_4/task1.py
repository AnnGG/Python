# Написати функцію < square > , яка прийматиме один аргумент
# - сторону квадрата, і вертатиме 3 значення (кортеж):
# периметр квадрата, площа квадрата та його діагональ.

from math import *
def square(x):

    perimeter = round(4 * x, 1)

    area_square = round(x * x, 1)

    diagonal = round(sqrt(x*x + x*x), 1)

    return perimeter, area_square, diagonal

side = float(input("Enter the side of the square "))

print("Perimeter, the area of ​​the square and the diagonal")

print(square(side))
