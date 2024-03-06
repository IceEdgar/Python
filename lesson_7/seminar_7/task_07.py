# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

group_ext = {
    'video': ['mov', 'avi', 'mkv'],
    'audio': ['mp3', 'ogg', 'wav'],
    'images': ['bmp', 'jpg', 'psd']
}


def sort_dir(directory: str):
    for file in os.listdir(directory):
        ext = file.split('.')[-1]
        for file_group, ext_group in group_ext.items():
            if ext in ext_group:
                if not os.path.exists(os.path.join(directory, file_group)):
                    os.mkdir(os.path.join(directory, file_group))
                shutil.move(os.path.join(directory, file), os.path.join(directory, file_group, file))


sort_dir('sample')