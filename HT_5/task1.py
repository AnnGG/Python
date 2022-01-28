# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
# і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True>
# - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException

class LoginException(Exception):

          pass

def login_password(username, password, silent = False):

     users = [["Ivan","12345"],["KL","mmmmLlll2"], ["Olga","123Kllg"],["Ira","kk35ooo"], ["Kira","k356ooo"]]

     try:
          if [username,password] in users:

               return True

          elif [username,password] not in users and silent == True:

               return False

          else:

               raise LoginException("Ops")

     except LoginException:

          print("Ops LoginException")

          
print("Input your username")

username = input()

print("Input your password")

password = input()

print("Input your Silence option(True/False)")

user_silent = input()

print("----Login Status----")

print(login_password(username, password, silent = user_silent == "True"))
