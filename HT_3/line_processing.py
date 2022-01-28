# Маємо рядок -->
# "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" ->
# просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

def line_processing(dsline):

    numbers = []

    letters = []

    for line in dsline:

        if line.isdigit():

            numbers.append(int(line))

        elif line.isalpha():

            letters.append(line)

    if 30 <= len(dsline) <= 50:

        print("The line length: ", len(dsline))

        print("The number of letters: ", len(letters))

        print("The number of digits: ", len(numbers))

    elif len(dsline) < 30:

        print("The sum numbers of list: ", sum(numbers))

        print("The line of letters: ", "".join(letters))

    else:

        for letter in letters:

            print("The string of double letters:")

            print(letter * 2, end="")
        

        
print("Input your string of digits and letters")

line_processing(input())
