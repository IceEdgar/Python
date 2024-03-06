"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import logging
import sys

logging.basicConfig(filename='Log/task_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def sum_and_product(frac1, frac2):
    """
    На вход подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
    Выводит сумму и произведение дробей.
    """

    # Разделение строк на числитель и знаменатель
    numer1, denom1 = map(int, frac1.split('/'))
    numer2, denom2 = map(int, frac2.split('/'))

    # Вычисление суммы дробей
    sum_numer = numer1 * denom2 + numer2 * denom1
    sum_denom = denom1 * denom2

    # Вычисление произведения дробей
    prod_numer = numer1 * numer2
    prod_denom = denom1 * denom2

    # Приведение дробей к несократимому виду
    gcd_sum = gcd(sum_numer, sum_denom)
    sum_numer //= gcd_sum
    sum_denom //= gcd_sum
    gcd_prod = gcd(prod_numer, prod_denom)
    prod_numer //= gcd_prod
    prod_denom //= gcd_prod

    # Вывод результатов
    # print(f"Сумма дробей: {sum_numer}/{sum_denom}")
    # print(f"Произведение дробей: {prod_numer}/{prod_denom}")
    return f"Сумма дробей: {sum_numer}/{sum_denom} \tПроизведение дробей: {prod_numer}/{prod_denom}"


def gcd(a, b):
    """Нахождение наибольшего общего делителя"""
    while b:
        a, b = b, a % b
    return a


def check_arg(data: str):
    if '/' in data:
        try:
            int(data.replace('/', ''))
            return True
        except ValueError:
            return False
    return False


if __name__ == '__main__':
    if len(sys.argv) < 3:
        msg = "Ошибка: необходимо указать два аргумента"
        print(msg)
        logger.error(msg)
        sys.exit(1)
    frac1 = sys.argv[1]
    frac2 = sys.argv[2]
    if not check_arg(frac1) or not check_arg(frac2):
        msg = f"Введены неверные аргументы: {frac1}, {frac2}"
        print(msg)
        logger.error(msg)
        sys.exit(1)
    logger.info(f'Переданные данные: {frac1}, {frac2}')
    result = sum_and_product(frac1, frac2)
    print(result)
    logger.info(result)

    # запуск из командной строки: python task_1.py 1/2 1/3