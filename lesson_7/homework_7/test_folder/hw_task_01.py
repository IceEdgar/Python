# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
# с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее
# счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

import os
import shutil
from pathlib import Path


def rename_files(source_ext: str,
                 target_ext: str,
                 path: str = os.getcwd(),  # Заменить на './test_folder' для автотестов
                 desired_name='',
                 num_digits=None,
                 limits: tuple = (),
                 ):
    count = 0
    for file in os.listdir(path):
        if file.endswith(source_ext):
            count += 1
            name = file.rsplit('.')
            if limits:
                re_name = f'{name[0][limits[0]:limits[1]]}{desired_name}{count:0>{num_digits}}.{target_ext}'
            else:
                re_name = f'{desired_name}{count:0>{num_digits}}.{target_ext}'

            os.rename(os.path.join(path, file), os.path.join(path, re_name))


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", limits=(3, 6))

# import os
#
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#
#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#
#     # Сортируем файлы по имени
#     filtered_files.sort()
#
#     # Задаем начальный номер для порядкового номера
#     num = 1
#
#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]
#
#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#
#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#
#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#
#         # Увеличиваем порядковый номер
#         num += 1

import os


def rename_files(desired_name=None, num_digits=3, source_ext=None, target_ext=None, name_range=[0, 0]):
    folder_path = "test_folder"

    files = [f for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f)) and f.endswith(f".{source_ext}")]

    files.sort()
    print(files)

    for idx, file_name in enumerate(files, start=1):
        original_name = file_name.split('.')[0][name_range[0] - 1:name_range[1]]
        new_name = f"{original_name}{desired_name}{idx:0{num_digits}d}.{target_ext}"
        os.rename(os.path.join("test_folder", file_name), os.path.join("test_folder", new_name))
        print(f"Переименован файл: {file_name} -> {new_name}")