#Написати скрипт, який отримує від користувача позитивне ціле число
# і створює словник, з ключами від 0 до введеного числа,
# а значення для цих ключів - це квадрат ключа.
# Приклад виводу при введеному значенні 5 :
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


n = int(input("Input your number: "))

d = dict()

for key_d in range(n + 1):

    if key_d not in d:

        d[key_d] = key_d * key_d

print("Your dictionary")
print(d)
