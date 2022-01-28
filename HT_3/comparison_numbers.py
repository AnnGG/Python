# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y"
# і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# -  Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z

def comparison_numbers(x, y):

    if x > y:

        result = x - y

        return("Вiдповiдь -", x, "бiльше нiж", y, "на", result)

    elif x < y:

        result = y - x

        return("Вiдповiдь -", y, "бiльше нiж", x, "на", result)

    else:

        return("Вiдповiдь -", "x =", x, "дорівнює", "y =", y)

x = int(input("Input x: "))

y = int(input("Input y: "))

answer= comparison_numbers(x, y)

print(*list(answer))
