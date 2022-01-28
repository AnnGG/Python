# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
# обробляє повернутий ними результат та також повертає результат.
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def len_numbers(numbers_list):

    return len(numbers_list)

def min_number(numbers_list):

    return min(numbers_list)

def max_number(numbers_list):

    return max(numbers_list)

def function_processing(number_list):

    result1 = len_numbers(number_list)

    result2 = min_number(number_list)

    result3 = max_number(number_list)

    return result1 + result2 + result3

print("The sum of the length maximum and minimum elements of the list")

print(function_processing([9, 21, 12, 1, 3, 15, 18]))
