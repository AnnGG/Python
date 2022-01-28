#Створити цикл від 0 до ... (вводиться користувачем).
#В циклі створити умову, яка буде виводити поточне значення,
#якщо остача від ділення на 17 дорівнює 0.

user_number = int(input("Input your number: "))

print("Numbers multiples of 17")

for number in range(user_number + 1):

    if number!= 0 and number%17 == 0:

        print(number, end=" ")

