"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def tobase(number: int, base: int):
    result = ""
    while number:
        temp_num = number % base
        if temp_num == 10:
            temp_num = "A"
        elif temp_num == 11:
            temp_num = "B"
        elif temp_num == 12:
            temp_num = "C"
        elif temp_num == 13:
            temp_num = "D"
        elif temp_num == 14:
            temp_num = "E"
        elif temp_num == 15:
            temp_num = "F"

        result = str(temp_num) + result
        number //= base
    return result


num = int((input("Введите число: ")))
print("Шестнадцатеричное представление числа: " + tobase(num, 16))
print("Проверка результата: " + hex(num))