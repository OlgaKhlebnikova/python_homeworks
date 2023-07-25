"""Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""


def print_menu(cash_print):
    """Функция для печати меню банкомата"""
    print("\nВаш текущий баланс = ", cash_print)
    print("МЕНЮ:".center(20))
    print("Добро пожаловать.", "Что вы хотите сделать?", "a - Пополнить баланс", "o - Снять наличные", "q - Выход",
          sep="\n")
    return cash_print


def put_money(cash_1_op, count_1_op):
    """Функция для внесения денег"""
    add = int(input("внесите сумму кратную 50: "))
    if add % 50 == 0:
        cash_1_op += add
        count_1_op += 1
        return cash_1_op, count_1_op
    else:
        print("Введена некорректная сумма (не кратна 50)")
        count_1_op += 1
        return cash_1_op, count_1_op


def give_money(cash_2_op, count_2_op):
    """Функция для снятия денег"""
    summ_out = int(input("введите сумму снятия кратную 50: "))
    if summ_out % 50 == 0:
        comission = summ_out * 0.015
        if comission < 30:
            comission = 30
        if comission > 600:
            comission = 600

        if cash_2_op < (summ_out + comission):
            print("Недостаточно средств")
            count_2_op += 1
            return cash_2_op, count_2_op
        else:
            cash_2_op -= (summ_out + comission)
            count_2_op += 1
            return cash_2_op, count_2_op
    else:
        print("Неверная сумма")
        count_2_op += 1
        return cash_2_op, count_2_op


def give_percent(cash_3_op, count_3_op):
    """Функция начисления процентов за каждую третью операцию в банкомате"""
    if count_3_op % 3 == 0:
        cash_3_op *= 1.03
        print(f"-> {count_3_op} Каждая 3-тья операция, банк начислил проценты, баланс = {cash_3_op:.2f}")
    return cash_3_op


def cash_machine(summ, count):
    """функция банкомата"""
    while True:
        if summ > 5_000_000:
            print("С вас сняли налог на богатство", summ * 0.1)
            summ -= summ * 0.1

        summ = print_menu(summ)

        action = input("\nваш выбор -> ")
        if action == "a":
            summ, count = put_money(summ, count)
        elif action == "o":
            summ, count = give_money(summ, count)
        elif action == "q":
            quit()
        summ = give_percent(summ, count)


# ----------------входные данные и запуск банкомата-----------------------
cash = 0
counter = 0
cash_machine(cash, counter)
