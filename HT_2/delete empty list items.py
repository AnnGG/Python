# Написати скрипт, який видалить пусті елементи із списка.
# Список можна "захардкодити".
# Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

list_with_empty_items = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]

list_with_not_empty_items = [items for items in list_with_empty_items if items]

print("Your list with not empty items")

print(list_with_not_empty_items)

    
