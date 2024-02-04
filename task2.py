BOOKS_DATABASE = [
    {
        "id": 45,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'  # Например, для строк важно указать !r


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if self.books==[]:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id):
        flag = False
        for book in enumerate(self.books):
            if book[1].id == id:
                flag = True
                return book[0]
        if flag == False:
            raise TypeError("Книги с запрашиваемым id не существует")

        # ids = []
        # for book in self.books:
        #     ids.append(book.id)
        #
        # if isinstance(ids.index(id),int):
        #     return ids.index(id)
        # else:
        #     raise TypeError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(45))  # проверяем индекс книги с id =
