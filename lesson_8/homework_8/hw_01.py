# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
# и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
# Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в
# байтах.
# Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной
# директории, и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории
# и возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных
# файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
# При этом сначала добавляются файлы, а затем директории.
# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), и
# затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results в
# виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
# Затем, для каждой директории (name в dirs), также создается полный путь к директории
# (path = os.path.join(root, name)), и вызывается функция get_dir_size(path),
# чтобы получить размер всей директории с учетом ее содержимого. Информация о директории добавляется в
# список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
import csv
import json
import os
import pickle
import sys
from pprint import pprint


def get_dir_size(dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += os.path.getsize(os.path.join(path, file))
    return total_size


def save_results_to_json(cur_path: str, source: list[str, dict]):
    name = os.path.join(cur_path, "result.json")
    with open(name, 'w', encoding='utf-8') as data:
        json.dump(source, data, indent=4, ensure_ascii=False)


def save_results_to_csv(cur_path: str, source: list[str, dict]):
    name = os.path.join(cur_path, "result.csv")
    file = [['Path', 'Type', 'Size']]
    for item in source:
        file.append([*item.values()])
    with open(name, 'w', encoding='utf-8') as data:
        csv_write = csv.writer(data, dialect='excel', delimiter=',', lineterminator="\n", )
        csv_write.writerows(file)


def save_results_to_pickle(cur_path: str, source: list[str, dict]):
    name = os.path.join(cur_path, "result.bin")
    with open(name, 'wb') as pickle_file:
        pickle.dump(source, pickle_file)


def traverse_directory(directory: str = os.getcwd()):

    list_res = []
    for path, dir_list, file_list in os.walk(directory):
        for cur_dir in dir_list:
            list_res.append({
                'Path': os.path.join(path, cur_dir),
                'Type': 'Directory',
                'Size': get_dir_size(os.path.join(path, cur_dir))})
        for cur_file in file_list:
            list_res.append({
                'Path': os.path.join(path, cur_file),
                'Type': 'File',
                'Size': os.path.getsize(os.path.join(path, cur_file))})


    return list_res


# result = [{85, 231413}, {2314, 2141}, {24, 432}]
# save_results_to_pickle('hw_task_01.py', result)
list_res = traverse_directory('D:\Архив сайтов')

save_results_to_json(os.getcwd(), list_res)
save_results_to_pickle(os.getcwd(), list_res)
save_results_to_csv(os.getcwd(), list_res)
with open('result.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

print(data)

'''
Код для автотеста
'''
# import csv
# import json
# import os
# import pickle
#
#
# def get_dir_size(directory):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(directory):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             total_size += get_dir_size(os.path.join(dirpath, d))
#     return total_size
#
#
# def traverse_directory(directory):
#     list_res = []
#     for path, dir_list, file_list in os.walk(directory):
#         for cur_file in file_list:
#             list_res.append({
#                 'Path': os.path.join(path, cur_file),
#                 'Type': 'File',
#                 'Size': os.path.getsize(os.path.join(path, cur_file))})
#         for cur_dir in dir_list:
#             list_res.append({
#                 'Path': os.path.join(path, cur_dir),
#                 'Type': 'Directory',
#                 'Size': get_dir_size(os.path.join(path, cur_dir))})
#
#     return list_res
#
#
# def save_results_to_json(source, name):
#     with open(name, 'w', encoding='utf-8') as data:
#         json.dump(source, data, indent=4, ensure_ascii=False)
#
#
# def save_results_to_pickle(source, name):
#     with open(name, 'wb') as pickle_file:
#         pickle.dump(source, pickle_file)
#
#
# def save_results_to_csv(source, name):
#     file = [['Path', 'Type', 'Size']]
#     for item in source:
#         file.append([*item.values()])
#     with open(name, 'w', encoding='utf-8') as data:
#         csv_write = csv.writer(data, dialect='excel', delimiter=',', lineterminator="\n", )
#         csv_write.writerows(file)
#
#
# results = traverse_directory(os.getcwd())
#
# save_results_to_pickle(results, 'results.pkl')
# save_results_to_json(results, 'results.json')
#
# save_results_to_csv(results, 'results.csv')

'''
Эталон
'''
# import os
# import json
# import csv
# import pickle
#
#
# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size
#
#
# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)
#
#
# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])
#
#
# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)
#
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results