"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак
препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
"""

#text = "Hello world. Hello Python. Hello again."
text = 'This is a sample text without repeating words.'
#text = "Python 3.9 is the latest version of Python. It's awesome!"
#text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
# Введите ваше решение ниже
# import re
#
# text_list = re.findall('\w+', text.lower())
# res = []
#
# for word in set(text_list):
#     if word in text_list:
#         res.append((word, text_list.count(word)))
#
# # res.sort(key=lambda a: (a[1],a[0]), reverse=True)
# print(res[:10])


user_words = []
word = ''
res = []
for char in text.lower():
    if char.isalpha():
        word += char
    else:
        if word:
            user_words.append(word)
        word = ''
else:
    if word:
        user_words.append(word)



for word in user_words:
    if word in user_words:
        res.append((word, user_words.count(word)))



encountered = {}
result = []
for tup in res:
    if tup not in encountered:
        encountered[tup] = True
        result.append(tup)

print(sorted(result, key=(lambda a: (a[1],a[0])), reverse=True)[:10])