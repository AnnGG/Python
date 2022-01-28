# Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран.
# Список можна "захардкодити".
# Елементами списку повинні бути як рядки, так і числа.


num_let_list = [2, "k", "word", 5, 6, "lllll"]

num_let_list = [str(i) for i in num_let_list]

num_let_list_str = "".join(num_let_list)

print("Your join list items")

print(num_let_list_str)
