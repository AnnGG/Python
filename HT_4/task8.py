# Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто, функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок,
# якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
# Наприклад:
#       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def move_elements(user_list, step):

    if step > 0:

        user_list = user_list[len(user_list)-step:len(user_list)] + user_list[0:len(user_list)- step]

        print("You have moved your list on ", step, " steps to the right")

        print(user_list)
    else:

        user_list = user_list[-step:] + user_list[0:(-step)]

        print("You have moved your list on ", step, " steps to the left")

        print(user_list)
    
print("Input step for move elements of list")

user_step = int(input())

user_list = [1,2,3,4,25,78,66,5,54]

print("Starting list")

print(user_list)

move_elements(user_list, user_step)
