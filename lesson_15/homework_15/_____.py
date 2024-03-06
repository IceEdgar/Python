# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование
import os
from collections import namedtuple
import logging
import argparse

FORMAT = '{asctime} : {funcName} - {levelname} - {msg}'
logging.basicConfig(filename='logger.log', filemode='w', encoding='UTF-8', format=FORMAT, style='{',
                    level=logging.NOTSET)
this_logger = logging.getLogger(__name__)

File = namedtuple('File', ['file_name', 'ext', 'parent_dir'])
Directory = namedtuple('Directory', ['dir_name', 'dir_flag', 'parent_dir'])

parser = argparse.ArgumentParser(description='Parser for directory_info script.')
parser.add_argument('-file_path', type=str, help='Enter path to desired directory')
args = parser.parse_args()


def directory_info(path_to_directory: str):
    this_logger.warning('Программа начала работу.')
    result = []
    for root, dirs, files in os.walk(path_to_directory):
        for file in files:
            file_name, ext = file.split('.')
            parent_dir = root.split('/')[-1]
            res = File(file_name, ext, parent_dir)
            result.append(res)
            this_logger.info(res)
        for directory in dirs:
            dir_name = directory
            parent_dir = root.split('/')[-1]
            path = os.path.join(root, directory)
            if os.access(path, os.W_OK):
                dir_flag = 'W'
            elif os.access(path, os.X_OK):
                dir_flag = 'X'
            else:
                dir_flag = 'R'
            res = Directory(dir_name, dir_flag, parent_dir)
            result.append(res)
            this_logger.info(res)
    this_logger.warning('Программа завершила работу.')
    return result


if __name__ == '__main__':
    directory_info(args.file_path)