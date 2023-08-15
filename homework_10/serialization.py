import json
import csv
import os
import pickle


class ToJson:
    def __init__(self, txt_file, json_file):
        """Инициализирует атрибуты"""
        self.txt_file = txt_file
        self.json_file = json_file

    def convert_txt_to_json(self):
        with open(self.txt_file, 'r', encoding='utf-8') as f, \
                open(self.json_file, "w", encoding='utf-8') as js_f:
            line = f.readlines()
            my_dict = {}
            for el in line:
                key, val = el.split("-")
                my_dict[key.title()] = float(val)
            return json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)



if __name__ == "__main__":
    my_object = ToJson('task7_3.txt', 'task8_1.json')
    my_object.convert_txt_to_json()
