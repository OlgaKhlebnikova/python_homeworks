"""
Задание №8

✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:

✔ Какие вещи взяли все три друга

✔ Какие вещи уникальны, есть только у одного друга

✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует

✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

data = {"Вова": ("шампур", "печеньки", "мясо", "вода"),
        "Саша": ("шоколад", "палатка", "вода", "бумага", "удочки"),
        "Маша": ("печеньки", "мяч", "бумага", "салфетки", "вода")}

set_all = set()
for j in data.values():
    set_all = set_all.union(set(j))
print(f"Вещи, которые взяли все три друга: {str(set_all)}\n")

# Какие вещи уникальны, есть только у одного друга
set_unique = set()
set_intersect = set()
for s in data:
    set_unique = set(data[s])
    for f in data:
        if s != f:
            set_unique = set_unique.difference(set(data[f]))
    if set_unique:
        print(f"Только {s} взял(а) {set_unique}")


for s in data:
    set_intersect = set(data[s])
    for f in data:
        if s != f:
            set_intersect = set_intersect.intersection(set(data[f]))
if set_intersect:
    print(f"\nВсе друзья взяли: {set_intersect}\n")



search = "бумага"
for f, things in data.items():
    if search not in things:
        print(f"{f} не взял(а) {search}")
    else:
        print(f"{f} взял(а) {search}")


