# Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Bunny(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Bunny.count += 1

    def display_count(self):
        print('Total bunnies: %d' % Bunny.count)

    def display_bunny(self):
        print('Bunny: {}'.format(self.name))

bunny = Bunny("Lulu")
bunny1 = Bunny("Marlen")

bunny.display_bunny()
bunny1.display_bunny()

print('Total bunnies: %d' % Bunny.count)