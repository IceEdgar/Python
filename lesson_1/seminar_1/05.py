"""
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""

steps = 5
figure = '*'
space = ' '
n_figure = 1
n_space = steps - 1

for _ in range(steps):
    print((n_space * space) + (n_figure * figure) + (n_space * space))
    n_figure += 2
    n_space -= 1