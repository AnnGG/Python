# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність
#(рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності,
# при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.

def infinite_generator(sequence_elements):

    i_sequence_elements = 0

    while True:

        if  i_sequence_elements == len(sequence_elements):

            i_sequence_elements = 0

        else:

            yield sequence_elements[i_sequence_elements]

            i_sequence_elements += 1
        


iterable_sequence = infinite_generator([1,2,3])

i=0

while True:

    print(next(iterable_sequence))
