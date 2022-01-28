# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів
# і повинен мати хоча б одну цифру; - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам
# - породити виключення із відповідним текстом.

def login_password(login, password):

    if len(login) < 3 or len(login) > 50:

        raise Exception("Username must be 3-50 characters long.")

    if len(password) < 8:

        raise Exception("The password is less than 8 characters long.")

    for i in password:

        if i.isdigit():

            break
    else:

        raise Exception("The password must contain at least one number.")

    for i in password:

        if i.isupper():

            break
    else:

        raise Exception("The password must contain at least one uppercase letter.")

    return("Welcome to the system")

login = input("Input your login: ")

password = input("Input your password: ")

print(login_password(login, password))
        
