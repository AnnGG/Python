# На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів
#(орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
# перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
# Name: vasya
# Password: wasd
# Status: password must have at least one digit
# -----
# Name: vasya
# Password: vasyapupkin2000
# Status: OK
# P.S. Не забудьте використати блок try/except ;)

def login_password(login, password):

     test=True

     if len(login) < 3 or len(login) > 50:

         raise Exception("Username must be 3-50 characters long.")

     if len(password) < 8:

         raise Exception("The password is less than 8 characters long.")

     for i in password:

         if i.isdigit():

             test=True

             break
         else:

             test=False

     if not test:
         raise Exception("The password must contain at least one number.")

     for i in password:

         if i.isupper():

             test=True

             break

         else:
             test=False

     if not test:

         raise Exception("The password must contain at least one uppercase letter.")

     return("Ok")


def check_users(users_login_password):

     for login, password in users_login_password.items():

         try:
             print("Name: ",login)

             print("Password: ", password)

             print("Status: ", login_password(login, password))

             print('-------------------------------------------')


         except:

             print("Status: User is not valid")

             print('-------------------------------------------')


         continue



users_login_password = {"Ivan":"kL45ooo0", "KL":"mmmmLlll2","Olga":"123Kllg", "Ira":"kk35ooo"}

check_users(users_login_password)
