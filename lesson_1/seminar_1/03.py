"""
Задание №6
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""

"""
def func(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 == 0:
        return 'yes'
    return 'no'
print(func(2023))
"""

in_year = int(input('Введите год:'))
CONST1 = 4
CONST2 = 100
CONST3 = 400

res = in_year % CONST1 == 0 and in_year % CONST2 != 0 or in_year % CONST3 == 0
print('Високосный' if res else 'Не високосный')