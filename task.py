class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        @property
        def pages(self):
            return self.pages

        @pages.setter
        def pages(self, new_pages: int) -> None:
            """Устанавливает количество страниц в книге."""
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть типа int")
            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть положительным числом")
            self.pages = new_pages

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._author!r}, {self.pages!r})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = duration

        @property
        def duration(self):
            return self.duration

        @duration.setter
        def duration(self, duration: float) -> None:
            """Устанавливает количество страниц в книге."""
            if not isinstance(duration, float):
                raise TypeError("Длительность должна быть типа float")
            if duration <= 0:
                raise ValueError("Длительность должна быть положительным числом")
            self.duration = duration

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._author!r}, {self.duration!r})'



