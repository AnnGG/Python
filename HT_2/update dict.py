# Написати скрипт, який об'єднає три словника в новий.
# Початкові словники не повинні змінитись. Дані можна "захардкодити".

# Sample Dictionary :
# dict_1 = {1:10, 2:20}
# dict_2 = {3:30, 4:40}
# dict_3 = {5:50, 6:60}

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}

dict_update = {}

dict_update.update(dict_1)
dict_update.update(dict_2)
dict_update.update(dict_3)

print("Your update dict")
print(dict_update)
