import argparse

parser = argparse.ArgumentParser(description='Принимает число, год для расчета')
parser.add_argument('-year', type=int, default=1900, help='Год для проверки')

args = parser.parse_args()
print(args)


def func(in_year):
    if in_year % 4 == 0 and in_year % 100 != 0 or in_year % 400 == 0:
        return 'Високосный'
    return 'Не високосный'


print(func(args.year))





