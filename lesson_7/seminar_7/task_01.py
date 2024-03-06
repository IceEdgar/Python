# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def write_numbers(file_name: str, count: int):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for _ in range(count):
            file.write(f'{randint(MIN_LIMIT, MAX_LIMIT)} | {uniform(MIN_LIMIT, MAX_LIMIT)}\n')


write_numbers('nums.txt', 10)