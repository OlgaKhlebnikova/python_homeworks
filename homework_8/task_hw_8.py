"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
from pathlib import Path
import json
import csv
import pickle


def get_dir_size(path='.') -> int:
    total_size = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_dir_size(entry.path)
    return total_size


def get_file_dir_size(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def directory_information(directory: Path):
    data = {}
    fieldnames = ['object_name', 'path', 'object_size', 'object_type', 'parent_directory']
    rows = []

    with open('j_result.json', 'w', encoding='utf-8') as f_json, open('c_result.csv', 'w', newline='',
                                                                      encoding='utf-8') as f_csv, open(
            'p_result.pickle', 'wb') as f_pickle:

        for dir_path, dir_name, file_name in os.walk(directory):
            data.setdefault(dir_path, {})
            for dir in dir_name:
                size = get_file_dir_size(dir_path + '/' + dir)
                data[dir_path].update(
                    {dir: {'object_size': size, 'object_type': 'directory',
                           'parent_directory': dir_path.split('\\')[-2]}})
                rows.append({'object_name': dir, 'path': dir_path, 'object_size': size, 'object_type': 'directory',
                             'parent_directory': dir_path.split('\\')[-2]})
            for i in file_name:
                size = get_file_dir_size(dir_path + '/' + i)
                data[dir_path].update(
                    {i: {'object_size': size, 'object_type': 'file', 'parent_directory': dir_path.split('\\')[-1]}})
                rows.append({'object_name': i, 'path': dir_path, 'object_size': size, 'object_type': 'file',
                             'parent_directory': dir_path.split('\\')[-1]})
        json.dump(data, f_json, indent=2)  # indent- количество отступов
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(data)}', f_pickle)


if __name__ == '__main__':
    directory_information(Path(Path.cwd()))
