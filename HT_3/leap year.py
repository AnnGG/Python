# Користувачем вводиться початковий і кінцевий рік.
# Створити цикл, який виведе всі високосні роки
# в цьому проміжку (границі включно).

print ("Enter start year")

start_year = int(input())

print ("Enter finish year")

finish_year = int(input())

print("Leap years")
 
for year in range(start_year, finish_year + 1):

    if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):

        print (year)
