# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint, choice

# vowels = ['e', 'u', 'o', 'a', 'y', 'i']
# consonat = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
#
# MIN_NAME = 4
# MAX_NAME = 7
# VOWEL = 1
# CONSONAT = 0
#
#
# def gen_name():
#     name = choice(consonat)
#     name_len = randint(MIN_NAME, MAX_NAME)
#     is_vowels = False
#     for i in range(1, name_len):
#         join_char = randint(CONSONAT, VOWEL)
#         if join_char:
#             is_vowels = True
#         name += choice(vowels) if join_char else choice(consonat)
#
#     if not is_vowels:
#         name += choice(vowels)
#     return name.capitalize()
#
#
# def write_names(count: int):
#     with open('names.txt', 'a', encoding='utf-8') as f:
#         for _ in range(count):
#             f.write(gen_name() + '\n')
#
#
# print(gen_name())
# write_names(3)


from random import randint, choice

consonant = set([chr(i) for i in range(ord('а'), ord('я') + 1)])
vowels = list('уеаоэяийюё')
consonant = list(consonant.difference(set(vowels)))
first_consonant = list(set(consonant).difference(set(list('ьыъ'))))

MIN_NAME = 4
MAX_NAME = 7


def generate_name(count: int):
    result = []
    for _ in range(count):
        name = choice(first_consonant)
        for i in range(1, randint(MIN_NAME, MAX_NAME)):
            name += choice(vowels) if i % 2 else choice(consonant)
        result.append(name.title())
    with open('names.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(result))


generate_name(10)