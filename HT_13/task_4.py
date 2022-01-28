# Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури»
# та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів
# доповнювали його та додавали початкові розміри.


class Figure(object):

    def __init__(self, color='white'):
        self.color = color

    def change_color(self, color):
        self.color = color


class Oval(Figure):

    def __init__(self, border_radius, color):
        super().__init__(color)
        self.border_radius = border_radius


class Square(Figure):

    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height


oval = Oval(2, "blue")
print(oval.border_radius, oval.color)

square = Square(4, 8, "red")
print(square.width, square.height, square.color)
