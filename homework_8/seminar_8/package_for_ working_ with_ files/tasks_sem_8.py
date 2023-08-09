import json
import csv
import os
import pickle

def convert_txt_to_json(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f,\
        open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)

def fun_dump_json(json_file):
    name = input("введите имя:> ")
    user_id = input("введите id:> ")
    level = int(input('введите уровень доступа (1-7):> '))
    # name = "Петя"
    # user_id = "002"
    # level = 4

    with open(json_file, "r", encoding='utf-8') as f:
        res = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open(json_file, "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)

def json_to_csv():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)

def read_csv_for_json_dict(csv_file, json_file):
    with open(csv_file, encoding="utf-8") as f:
        f_r = csv.reader(f)
        res = list(f_r)
        for i in range(1, len(res)):
            temp = res[i][1]
            res[i][1] = f"{temp.zfill(10)}"
            res[i][2] = res[i][2].title()
    with open(json_file,"w", encoding="utf-8") as j:
        json.dump(res,j)

def search_rename_json_pickle():
    for el in os.listdir():
        if el.endswith(".json"):
            with open(el, "r", encoding="utf-8") as j:
                res = json.load(j)
            path = ''.join(el.split(".")[:-1]) + ".pickle"
            with open(path, "wb") as p:
                pickle.dump(res, p)

def pickle_for_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    with open(csv_file, "w", encoding="utf-8") as c:
        writer = csv.writer(c)
        for row in data:
            writer.writerow(row)

def read_csv_str_pickle(csv_file):
    with open(csv_file, "r", encoding="utf-8") as c:
        rider = csv.reader(c)
        print(pickle.dumps(list(rider)))

if __name__ == "__main__":
    convert_txt_to_json('task7_3.txt', 'task8_1.json')
    fun_dump_json('task8_2.json')
    json_to_csv()
    read_csv_for_json_dict('task8_2.csv', 'new_json.json')
    pickle_for_csv('new_json.pickle', "new_c.csv")
    read_csv_str_pickle("new_c.csv")