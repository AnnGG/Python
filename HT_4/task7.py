# Написати функцію, яка приймає на вхід список
# і підраховує кількість однакових елементів у ньому.


def frequency_elements(list_elements):

    frequency_element = {}

    for element in list_elements:

        if element in frequency_element:

            frequency_element[element] += 1

        else:

            frequency_element[element] = 1

    for element, freq_element in frequency_element.items():

        print("Element ", element, " - ", freq_element, " times")

print("Enter a sequence of items on one line separated by a space")

user_list = input().split()

frequency_elements(user_list)

            

    
