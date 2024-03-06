"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
import argparse
import logging
import os
import re


logging.basicConfig(filename='Log/task_2.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def count_occurring_words(text):
    """
    В большой текстовой строке text подсчитывает количество встречаемых слов и возвращает 10 самых частых.
    Не учитывает знаки препинания и регистр символов.
    Слова разделяются пробелами, апостроф не считается за пробел.
    Такие слова как dont, its, didnt итд (после того, как убрали знак препинания апостроф) считаются одним словом.
    """
    data = re.sub(r'[^\w\s]+|\d', '', text.lower()
                  .replace('-', ' ').replace("'", ' '))
    data = data.split(' ')

    tmp = []
    words_count = []
    for w in data:
        if w not in tmp and w != '':
            tmp.append(w)
            words_count.append((w, data.count(w)))

    for limit in range(len(words_count) - 1, 0, -1):
        for i in range(limit):
            if words_count[i][1] < words_count[i + 1][1]:
                words_count[i], words_count[i + 1] = words_count[i + 1], words_count[i]

    return words_count[:10]


if __name__ == '__main__':
    # test_text = ("Python is an interpreted, high-level, general-purpose programming language. "
    #              "Created by Guido van Rossum and first released in 1991, Python's design philosophy "
    #              "emphasizes code readability with its notable use of significant whitespace. "
    #              "Its language constructs and object-oriented approach aim to help programmers write clear, "
    #              "logical code for small and large-scale projects.")
    # print(*count_occurring_words(test_text))

    parser = argparse.ArgumentParser(description="Принимает путь до текстового файла")
    parser.add_argument('file_path', type=str, help='Путь до файла', default='example.txt')
    args = parser.parse_args()
    file_path = args.file_path
    if not os.path.isfile(file_path):
        msg = f'Указан неверный путь: {file_path}'
        logger.error(msg)
        print(msg)
        exit(1)
    logger.info(f"Указан файл: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    res_msg = "Наиболее часто встречаемые слова:\n"
    for el in count_occurring_words(data):
        res_msg = res_msg + str(el) + ' '
    logger.info(res_msg)
    print(res_msg)

    # запуск из командной строки: python task_1.py example.txt