'''
Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''
import  argparse
import logging
from collections import namedtuple
import  os
FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False, ''])   # (имя файла, расширение, директория или нет, родительская директория) - кортеж
FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='hw15t01_file_list.txt', filemode='w', format=FORMAT, style='{', level=logging.NOTSET)
common_log = logging.getLogger()

if __name__ == '__main__':
    print("Not for separate use")

def parse_ars():
    parser = argparse.ArgumentParser(description="hw15t01_s15t06")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))

def walk_dir(path_string: str):
    fs_objects = []
    if not path_string:
        path_string = os.getcwd()
        common_log.warning(f'Путь установлен по умолчанию {path_string}')
    path_string = os.path.abspath(path_string)
    parent = path_string.rstrip('/').rsplit('/', 1)[1]          # получаем абсолютный путь
    try:
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            item: str = item.rsplit('/',1)[1]
            if item.rfind('.') != -1 and not item.startswith('.'):
                obj_name, obj_ext = item.rsplit('.', 1)
            else:
                obj_name = item
            fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
        common_log.info(msg=str(fs_objects[-1]))
    except Exception as exc:
        print(f'\033[31mERRORR: {exc.__class__.name__}: {exc}\033[0m')
        common_log.error(msg=f'{exc.__class__.name__}: {exc}')
    return fs_objects                                   # список наименованных кортежей

if __name__ == '__main__':
    print('Not for separate use')

if __name__ == '__main__':
    main()
# Seminar_15/Task6.py -p hw15_utils ../task1  - запуск из командной строки