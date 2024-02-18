class Shape:
    def __init__(self, color):
        """
        Создание объекта "Фигура"

        :param colour: цвет фигуры

        Примеры:
        >>> fig1 = Shape("Blue")  # инициализация экземпляра класса
        """

        self.color = color

    def display_color(self):
        print("Цвет фигуры:", self.color)

    def __str__(self):
        return f"Фигура ({self.color})"

    def __repr__(self):
        return f"Shape({self.color})"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        """
        Создание объекта "Прямоугольник", дочернего класса "Фигуры"
        color: цвет, наследуемый параметр
        width: ширина
        height: высота
        Примеры:
        >>> rectangle = Rectangle("Красный", 5, 3)
        """
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        :return: Площадь прямоугольника.
        >>> rectangle = Rectangle("Красный", 5, 3)
        >>> a = rectangle.calculate_area
        """
        area = self.width * self.height
        print("Площадь прямоугольника:", area)
        return area

    def calculate_perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника.

        :return: Периметр прямоугольника.

        >>> rectangle = Rectangle("Красный", 5, 3)
        >>> a = rectangle.calculate_perimeter
        """
        perimeter = 2 * (self.width + self.height)
        print("Периметр прямоугольника:", perimeter)
        return perimeter

    def __str__(self):
        return f"Прямоугольник (ширина: {self.width}, высота: {self.height}, цвет: {self.color})"

    def __repr__(self):
        return f"Rectangle({self.color}, {self.width}, {self.height})"


if __name__ == "__main__":
    pass