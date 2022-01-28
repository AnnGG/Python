# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року,
# якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(number_month):

    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if number_month in winter:

        return "Winter"

    elif number_month in spring:

        return "Spring"

    elif number_month in summer:

        return "Summer"

    elif number_month in autumn:

        return "Autumn"

    else:

        return "This month is not on the calendar"

print(season(int(input("Input your number of month: "))))
