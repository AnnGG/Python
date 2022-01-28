# Написати скрипт, який залишить в словнику тільки пари
# із унікальними значеннями (дублікати значень - видалити).
# Словник для роботи захардкодити свій.
# Приклад словника (не використовувати):
# {'a': 1, 'b': 3, 'c': 1, 'd': 5}
# Очікуваний результат:
# {'a': 1, 'b': 3, 'd': 5}


users_list = {

     "Tom": "+11111111",
     "Bob": "+33333333",
     "Alice": "+55555555",
     "Elen": "+11111111"
}

new_users_list = {}

for names, phone_numbers in users_list.items():

    if phone_numbers not in new_users_list.values():

        new_users_list[names] = phone_numbers

print("New users list")
print(new_users_list)

    


