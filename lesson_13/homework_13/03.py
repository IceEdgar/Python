# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.
MIN_ID = 100_000
MAX_ID = 1_000_000


class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message


class Validate:
    """Descriptor for validation errors in Person objects"""

    def __init__(self, message):
        self.param_name = None
        self.message = message

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"You don't have permission to delete  {self.param_name}")

    def validate(self, value):
        if self.message == 'nonempty string':
            if not isinstance(value, str) or value == '':
                raise InvalidNameError(f'Invalid name: {value}. Name should be a non-empty string.')
        if self.message == 'positive integer':
            if not isinstance(value, int) or value <= 0:
                raise InvalidAgeError(f'Invalid age: {value}. Age should be a positive integer.')
        if self.message == 'six digits positive integer':
            if not isinstance(value, int) or value not in range(MIN_ID, MAX_ID):
                raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 '
                                     f'and 999999.')


class Person:
    surname = Validate('nonempty string')
    name = Validate('nonempty string')
    patronymic_name = Validate('nonempty string')
    age = Validate('positive integer')

    def __init__(self, surname: str, name: str, patronymic_name: str, age: int):
        self.surname = surname
        self.name = name
        self.patronymic_name = patronymic_name
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic_name}, age={self.age}'

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    u_id = Validate('six digits positive integer')

    def __init__(self, surname: str, name: str, patronymic_name: str, age: int, u_id: int):
        super().__init__(surname, name, patronymic_name, age)
        self.u_id = u_id

    def get_level(self):
        res = 0
        start = self.u_id
        while start > 0:
            res += start % 10
            start = start // 10
        return res % 7


if __name__ == '__main__':
    p1 = Person('Иванов', 'Иван', 'Иванович', 23)
    print(p1)
    p1.birthday()
    print(p1)
    e1 = Employee('Петров', 'Петр', 'Петрович', 34, 781321)
    print(e1.get_level())

    print(e1.get_age())