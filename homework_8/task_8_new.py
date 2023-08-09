import os
import csv
import json
import pickle
def directory_information(directory):
    size_sum_all = 0
    dict_dir = dict()
    for path, my_dir, file_2 in os.walk(directory):
        dict_dir[os.path.dirname(path)] = {path: {i: None for i in file_2}}
        print(f"\n> Родительская директория: {os.path.dirname(path)}")
        print(f'  > Путь данной директории: {path} \n    > Каталог(и): \\{"нет" if my_dir == [] else ", ".join(my_dir)}')
        size_sum = 0
        if file_2:
            print(f'>  Найдено {len(file_2)} файл(а): ')
            for i, name_file in enumerate(file_2, start=1):
                size = path + "\\" + name_file
                size_sum += os.stat(size).st_size
                print(f"{i}-ый файл: имя{name_file :_>20}, размер{os.stat(size).st_size:_>40} байт")
                dict_dir[os.path.dirname(path)][path][name_file] = str(os.stat(size).st_size) + " байт"
        else:
            print("> Файлов нет")
            dict_dir[os.path.dirname(path)] = {path: "файлы не найдены"}
        print(f"Общий размер{size_sum:_>70} байт" if file_2 else "")
        size_sum_all += size_sum
    print(f"Общий размер исходной директории{size_sum_all:_>70} байт")
    dict_dir.update(Общий_размер_исходной_директории=str(size_sum_all) + " байт")

    with open('result.json', 'w', encoding='utf-8') as file_2:
        json.dump(dict_dir, file_2, indent=2, ensure_ascii=False)
    with open('result.pickle', 'wb') as file_2:
        pickle.dump(dict_dir, file_2)
    with open('result.csv', 'w', newline='', encoding="utf-8") as file_3:
        writer = csv.writer(file_3, delimiter=" ")
        for i, j in dict_dir.items():
            writer.writerow((i, j))
            if isinstance(j, dict):
                for k, y in j.items():
                    writer.writerow((k, y))
                    if isinstance(y, dict):
                        for q, w in y.items():
                            writer.writerow((q, w))


my_way = "'D:\\ОБУЧЕНИЕ\\GB\\Python\\погружение\\python_homeworks\\homework_8'"
directory_information(my_way)