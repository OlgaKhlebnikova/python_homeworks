"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых"""
import csv
import json

class Validator:
    def __init__(self, name_full: str = None):
        self.name_full = name_full

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')

class Student:
    name = Validator()
    lastname = Validator()
    patronymic = Validator()
    grade_res = 'оценки'
    test_res = 'результаты тестирования'

    def __init__(self, name,  patronymic, lastname,):
        self.name = name
        self.lastname = lastname
        self.patronymic = patronymic
        self.__study_journal = dict()
        with open('lessons.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter="\n")
            for row in file_reader:
                self.__study_journal[str(*row)] = {self.grade_res: [], self.test_res: []}

    def rate_student(self, subject: str, evaluate: int):
        if   self.__study_journal.get(subject) is None:
            raise AttributeError(f'В расписании студента нет данного предмета')
        if not 1 < evaluate < 6:
            raise ValueError('оценки (от 2 до 5)')
        self.__study_journal[subject][self.grade_res].append(evaluate)

    def test_score(self, subject: str, score: int):
        if self.__study_journal.get(subject) is None:
            raise AttributeError(f'В расписании студента нет данного предмета')
        if not -1 < score < 101:
            raise ValueError('результаты тестов (от 0 до 100)')
        self.__study_journal[subject][self.test_res].append(score)

    def average_score(self, subject, what_result):
        if self.__study_journal[subject][what_result]:
            result = sum(self.__study_journal[subject][what_result]) \
                     / len(self.__study_journal[subject][what_result])
            return f'Средние {what_result} по предмету "{subject}": {result} балла.'
        return f'Средние {what_result} по предмету "{subject}": оценки отсутствуют.'

    def overall_point_average(self):
        summ = 0
        count = 0
        for i in self.__study_journal:
            summ += sum(self.__study_journal[i][self.grade_res])
            count += len(self.__study_journal[i][self.grade_res])
        return round(summ / count, 2)

    def __repr__(self):
        return f'Student(name="{self.name}", patronymic="{self.patronymic}", lastname="{self.lastname}")'

    @property
    def study_journal(self):
        return self.__study_journal


if __name__ == '__main__':
    grade = 'оценки'# чтобы учесть отдельно оценки
    test = 'результаты тестирования'# чтобы учесть отдельно тестирование
    student_1 = Student('Иван', 'Петрович', 'Сидоров')
    print(student_1)

    # оценки
    student_1.rate_student('Химия', 4)
    student_1.rate_student('Обществознание', 5)
    student_1.rate_student('История', 4)
    student_1.rate_student('Физика', 5)


    # тестирование
    student_1.test_score('Химия', 95)
    student_1.test_score('Химия', 100)
    student_1.test_score('Физика', 89)
    student_1.test_score('Физика', 76)

    # результат, оценки (средний балл)
    print(student_1.average_score('Химия', grade))
    print(student_1.average_score('Обществознание', grade))
    print(student_1.average_score('История', grade))
    print(student_1.average_score('Физика', grade))
    print(student_1.average_score('Химия', test))
    print(student_1.average_score('Обществознание', test))

    print(f'Средний балл студента  = {student_1.overall_point_average()}')

    # для наглядности)
    with open('оценки.json', 'w', encoding='utf-8') as file_json:
        json.dump(student_1.study_journal, file_json, ensure_ascii=False, indent=4)

    #Проверка ошибок
    student_1.rate_student('Химия', 1)
    student_1.rate_student('Математика', 4)
    student_1.test_score('Математика', 100)