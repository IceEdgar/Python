# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

code_to_write = """
import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='', encoding='utf-8', ) as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


def save_to_json(func):
    def wrapper(file_name):
        res = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result = {"parameters": [a, b, c], "result": roots}
                res.append(result)
        with open('results.json', 'w', encoding='utf-8') as file:
            json.dump(res, file, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        return None
    elif discr == 0:
        return -b / (2 * a)
    else:
        root_1 = (-b + discr ** 0.5) / 2 * a
        root_2 = (-b - discr ** 0.5) / 2 * a
        return root_1, root_2
"""

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)