# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from pack_task_04 import create_files


def generation_some_files_extensions(directory: str, **kwargs):
    if kwargs:
        for extension, count in kwargs.items():
            create_files(directory, extension, count=count)


generation_some_files_extensions('sample', avi=5, mov=4, mkv=2, mp3=5, ogg=4, wav=4,
                                 bmp=6, jpg=2, psd=8, txt=2, doc=3)