"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.

Для проверки своего кода используйте модуль fractions.
"""

frac1 = "1/6"
frac2 = "2/3"


# Введите ваше решение ниже

def sum_fraction(numerator_1, numerator_2, denominator_1, denominator_2):
    common_denominator = int(denominator_1) * int(denominator_2)
    sum_numerators = (int(numerator_1) * int(denominator_2) +
                      int(numerator_2) * int(denominator_1))
    answer = f'{sum_numerators}/{common_denominator}'
    return answer


def mult_fraction(numerator_1, numerator_2, denominator_1, denominator_2):
    mult_numerators = int(numerator_1) * int(numerator_2)
    mult_denominators = int(denominator_1) * int(denominator_2)
    answer = f'{mult_numerators}/{mult_denominators}'
    return answer


def numerator(user_fraction: str):
    user_numerator_fraction = ''
    for i in range(len(user_fraction)):
        if user_fraction[i].isdigit():
            user_numerator_fraction = user_numerator_fraction + user_fraction[i]
        else:
            return user_numerator_fraction
    return user_numerator_fraction


def denominator(user_fraction: str):
    user_denominator_fraction = ''
    rev_user_fraction = user_fraction[::-1]
    for i in range(len(rev_user_fraction)):
        if rev_user_fraction[i].isdigit():
            user_denominator_fraction = rev_user_fraction[i] + user_denominator_fraction
        else:
            return user_denominator_fraction
    return user_denominator_fraction


user_numerator_frac1 = numerator(frac1)
user_numerator_frac2 = numerator(frac2)
user_denominator_frac1 = denominator(frac1)
user_denominator_frac2 = denominator(frac2)
print("Сумма дробей: " + sum_fraction(user_numerator_frac1, user_numerator_frac2,
                                      user_denominator_frac1, user_denominator_frac2))
print("Произведение дробей: " + mult_fraction(user_numerator_frac1, user_numerator_frac2,
                                              user_denominator_frac1, user_denominator_frac2))