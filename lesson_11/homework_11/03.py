"""
Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.

Атрибуты класса:

width (int): Ширина прямоугольника. height (int): Высота прямоугольника.

Методы класса:

__init__(self, width, height=None): Конструктор класса. Принимает ширину и высоту прямоугольника. Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом, и высота устанавливается равной ширине.

perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.

area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.

__add__(self, other): Магический метод, который определяет операцию сложения (+) для двух прямоугольников. Принимает другой прямоугольник other. Создает новый прямоугольник, который представляет собой объединение исходных прямоугольников по периметру. Возвращает новый прямоугольник.

__sub__(self, other): Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого. Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу периметров исходных прямоугольников, и вычисляет высоту на основе этой разницы. Возвращает новый прямоугольник.

__lt__(self, other): Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади второго, иначе False.

__eq__(self, other): Магический метод, который определяет операцию "равно" (==) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площади равны, иначе False.

__le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше или равна площади второго, иначе False.

__str__(self): Магический метод, возвращающий строковое представление прямоугольника. Возвращает строку, описывающую ширину и высоту прямоугольника.

__repr__(self): Магический метод, возвращающий строковое представление прямоугольника, которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.

Пояснение:

Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников, и создает новый прямоугольник.
Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.

Пример использования:
На входе:

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")

На выходе:

Периметр rect1: 30
Площадь rect2: 21
rect1 < rect2: False
rect1 == rect2: False
rect1 <= rect2: False
Периметр rect3: 50
Ширина rect4: 2




class Rectangle:
    def __init__(self, len_rec, width=None):
        self.len_rec = len_rec
        self.width = len_rec if width is None else width

    def perimeter(self):
        return 2 * (self.len_rec + self.width)

    def area(self):
        return self.len_rec * self.width

    def __add__(self, other):
        return Rectangle(self.len_rec + other.len_rec, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.len_rec - other.len_rec), abs(self.width - other.width))

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __str__(self) -> str:
        return f"Прямоугольник со сторонами {self.len_rec} и {self.width}"

    def __repr__(self) -> str:
        return f"Rectangle({self.len_rec}, {self.width})"


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")
"""
import math
class Rectangle():

    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = height
        if height == None:
            self.height = width

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(self.width - other.width, self.height - other.height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(4)
rect4 = rect1 + rect2
rect5 = rect1 - rect2


print(repr(rect1))
print(repr(rect2))
print(repr(rect3))
print(repr(rect4))
print(repr(rect5))

print(rect1)
print(rect2)
print(rect3)

print(rect1.perimeter())
print(rect2.perimeter())
print(rect1.area())

print(rect1 < rect2)
print(rect1 == rect2)
print(rect2 <= rect1)

'''
# Введите ваше решение ниже
class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"

'''