import doctest
from typing import Union


class Mesh:
    def __init__(self, X_edge: float, Y_edge: float):
        """
        Создание и подготовка к работе объекта "Сетка"
        прямоугольная область на координатной плоскости с началом в точке (0, 0)

        :param X_edge: граница области по оси X
        :param Y_edge: граница области по оси Y
        аттрибуты cells, s, nodes определяются в методах
        Примеры:
        >>> mesh = Mesh(10, 20)  # инициализация экземпляра класса
        """

        self.cells = None
        self.s = None
        self.nodes = None

        if not isinstance(X_edge, (int, float)):
            raise TypeError("граница области по оси X должна быть типа int или float")
        self.X_edge = X_edge

        if not isinstance(Y_edge, (int, float)):
            raise TypeError("граница области по оси Y должна быть типа int или float")
        self.Y_edge = Y_edge

    def square(self) -> float:
        """
        Функция которая ищет площадь области и записывает значение в аттрибут
        :return: площадь области

        Примеры:
        >>> mesh2 = Mesh(50, 2)
        >>> mesh2.square()
        100
        """
        self.s = self.X_edge * self.Y_edge
        return self.X_edge * self.Y_edge

    def fraction(self, n: int) -> None:
        """
        Функция которая ищет дробит область
        и записывает получившееся количество ячеек в аттрибут cells
        а также считает координаты получившехся при разбиении точек
        и записывает их в аттрибут nodes

        Примеры:
        >>> mesh = Mesh(50, 2)
        >>> mesh.fraction(6)
        """
        if not (isinstance(n, int) and n > 0):
            raise TypeError("дробить можно только натуральным числом")

        self.cells = n * n
        self.nodes = ...


class Room:
box_types = {"red": 1.2, "blue": 2}

def __init__(self, total_area:  float, occupied_area: float):
    """
    Создание и подготовка к работе объекта "Комната"

    :param total_area: площадь всей комнаты
    :param occupied_area: занятая площадь комнаты
    Примеры:
    >>> room_121 = Room(51.0, 2.1)  # инициализация экземпляра класса
    """

    self.free = total_area - occupied_area  # свободная площадь
    self.all_boxes = None # словарь содержащий типы коробок и их количество

    if not (isinstance(total_area, (int,float)) & (total_area > 0)):
        raise TypeError("площадь комнаты должна быть положительным числом")
    self.total_area = total_area

    if not (isinstance(occupied_area, (int,float)) & (occupied_area > 0)):
        raise TypeError("занятая площадь комнаты должна быть положительным числом")
    self.occupied_area = occupied_area

def add(self, box_type: str, num: int) -> None:
    """
    Функция которая добавляет в комнату заданное
    количество коробок заданного типа тем самым
    увеличивает занимаемую площадь
    :param box_type: тип добавляемых коробок
    :param num: количество добавляемых коробок

    Примеры:
    >>> room121 = Room(40, 15)
    >>> room121.add("red", 5)
    """
    if not (self.free < 20): # 20 взято для примера
        ...
        # raise ValueError("недостатночно свободного места")
    if not isinstance(num, int):
        raise TypeError("количество коробок должно быть целым числом")
    if not isinstance(box_type, str):
        raise TypeError("неверный тип коробки")

def max_load(self) -> dict:
    """
    Функция которая считает какую максимальную площадь можно заполнить

    :return: словарь с типами и количеством коробок,
    соответствующий максимальному заполнению комнаты

    Примеры:
    >>> room44 = Room(50, 2)
    >>> room44.max_load()
    """
    if self.free < 10:
        raise ValueError("комната заполнена")
    ...

class Mesh:
    def __init__(self, X_edge: float, Y_edge: float):
        """
        Создание и подготовка к работе объекта "Сетка"
        прямоугольная область на координатной плоскости с началом в точке (0, 0)

        :param X_edge: граница области по оси X
        :param Y_edge: граница области по оси Y
        аттрибуты cells, s, nodes определяются в методах
        Примеры:
        >>> mesh = Mesh(10, 20)  # инициализация экземпляра класса
        """

        self.cells = None
        self.s = None
        self.nodes = None

        if not isinstance(X_edge, (int, float)):
            raise TypeError("граница области по оси X должна быть типа int или float")
        self.X_edge = X_edge

        if not isinstance(Y_edge, (int, float)):
            raise TypeError("граница области по оси Y должна быть типа int или float")
        self.Y_edge = Y_edge

    def square(self) -> float:
        """
        Функция которая ищет площадь области и записывает значение в аттрибут
        :return: площадь области

        Примеры:
        >>> glass = Mesh(50, 2)
        >>> glass.square()
        100
        """
        self.s = self.X_edge * self.Y_edge
        return self.X_edge * self.Y_edge

    def fraction(self, n: int) -> None:
        """
        Функция которая ищет дробит область
        и записывает получившееся количество ячеек в аттрибут cells
        а также считает координаты получившехся при разбиении точек
        и записывает их в аттрибут nodes

        Примеры:
        >>> mesh = Mesh(50, 2)
        >>> mesh.fraction(6)

        """
        if not (isinstance(n, int) and n > 0):
            raise TypeError("дробить можно только натуральным числом")

        self.cells = n * n
        self.nodes = ...


class Student:
    all_courses = ["a", "b", "c"]  # список всех возможных курсов, для дальнейшего использования в методах

    def __init__(self, name: str, courses: list[str]):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: имя студента
        :param courses: список посещаемых курсов

        Примеры:
        >>> stud1 = Student("John", ["math", "art"])  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть в формате строки")
        if not isinstance(courses, list):
            raise TypeError("Требуется список курсов")

        self.name = name
        self.courses = courses

    def number_of_courses(self) -> int:
        """
        Функция которая возвращает количество курсов студента

        :return: количество курсов

        Примеры:
        >>> stud2 = Student("tom", ["bc", "bce"])
        >>> stud2.number_of_courses()
        """
        ...

    def add_course(self, course: str) -> None:
        """
        Добавление курса студенту.
        :param course: название курса

        Примеры:
        >>> stud3 = Student("bob", ["qw", "ert"])
        >>> stud3.add_course(Student.all_courses[1])
        """
        if not isinstance(course, str):
            raise TypeError("тип курса должен быть строкой")
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
