# Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color
# з початковим значенням white і метод для зміни кольору фігури,
# а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__
# для завдання початкових розмірів об'єктів при їх створенні.


class Figure(object):

    color = 'white'

    def change_color(self, color):

        self.color = color


class Oval(Figure):

    def __init__(self, border_radius):

        self.border_radius = border_radius


class Square(Figure):

    def __init__(self, width, height):

        self.width = width
        self.height = height


oval = Oval(2)
oval.change_color('blue')
print(oval.border_radius, oval.color)

square = Square(4, 8)
square.change_color('red')
print(square.width, square.height, square.color)


