# Задание №4
# Работа в консоли в режиме интерпретатора Python.
# Решите квадратное уравнение
# 5x**2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c. https://younglinux.info/python/task/quadratic

from math import sqrt

a, b, c, = 5, -10, -400
d = (b ** 2) - (4 * a * c)
if d < 0:
    print("корней нет")
elif d > 0:
    x1 = (sqrt(d) - b) / (2 * a)
    x2 = (-sqrt(d) - b) / (2 * a)
    print(f'корни {x1, x2}')
elif d == 0:
    print((-b) / 2 * a)


