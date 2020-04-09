"""
0. написать программу, которая спросит у пользователя имя и отчество.
и поприветствует его как "Здравствуйте, уважаемый Семен Семенович !"
(с восклицательным знаком в конце)
"""
def hello_username():
    while True:
        first_name = input("Введите свое имя: ")
        middle_name = input("Введите свое отчество: ")

        if first_name.isalpha() and middle_name.isalpha():
            print('Здравствуйте, уважаемый %s %s !' % (first_name,middle_name))
            break
        elif not first_name or not middle_name:
            print("Пустая строка, попробуйте еще раз")
        else:
            print("Неправильный формат данных, попробуйте еще раз")

hello_username()

"""
А. написать программу перевода миль в футы. Для этого количество миль нужно умножить на 5280.
"""
miles = float(input("Enter number of miles: "))
feet = miles*5280
print("Feet:", feet)

"""
Б. написать программу перевода градусов Фаренгейта в градусы Цельсия. 
Для этого нужно от числа градусов фаренгейта отнять 32, результат умножить на 5 и затем поделить на 9.
"""
fahr = float(input("Enter Fahrenheit temperature: "))
celsius = (fahr - 32)*5/9
print("Celsius:", round(celsius,2))

"""
С. (Bonus points, необязательное) написать программу перевода градусов Цельсия в Фаренгейты.
"""

cels = float(input("Enter Celsius temperature: "))
fahrenheit = (cels * 9/5) + 32
print("Fahrenheit:", round(fahrenheit,2))
