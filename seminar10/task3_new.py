class Human:

    def __init__(self, last_name, first_name, age):
        self._last_name = last_name
        self._first_name = first_name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 70:
            raise ValueError('староват')
        self.__age = value

    def up_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'


if __name__ == "__main__":
    person = Human('Smith', 'Johan', 40)

    # print(person._first_name)
    # # print(person.__age())
    # print(person.get_age())
    # person.up_birthday()
    # print(person.get_age())
    # print(person.get_fullname())
    person.age = 80
    print(person.age)