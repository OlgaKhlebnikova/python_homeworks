"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
каждое число от test до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

from queen_move import battle_queens


def check_battle(position: tuple):
    if battle_queens(position):
        print(" Ферзи не бьют друг друга ")
    else:
        print(" Ферзи бьют друг друга ")

if __name__ == "__main__":

    position_1 = (1, 1), (2, 2), (3, 2), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)  # ферзи бьют друг друга
    position_2 = (1, 9), (2, 6), (3, 2), (4, 5), (5, 8), (6, 1), (7, 7), (8, 4)  # ферзи не бьют друг друга
    check_battle(position_1)
    check_battle(position_2)