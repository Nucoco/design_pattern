# Implementation of interfaces with standard library
from collections.abc import Iterator, Iterable


class Book:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# ConcreteAggregate
class BookShelf(Iterable):

    def __init__(self):
        self.__books = []

    def append_book(self, book: Book):
        self.__books.append(book)

    def get_book_at(self, index):
        return self.__books[index]

    def __iter__(self):
        print('Created Iterator')
        return BookShelfIterator(self)


# ConcreteIterator
class BookShelfIterator(Iterator):

    def __init__(self, book_shelf: BookShelf, reverse=False):
        self.__book_shelf = book_shelf
        self.__index = -1 if reverse else 0
        self.__reverse = reverse

    def __next__(self):
        try:
            print(f'try: {self.__index}')
            book = self.__book_shelf.get_book_at(self.__index)
            self.__index += -1 if self.__reverse else 1
        except:
            raise StopIteration()

        return book


book_shelf = BookShelf()
book_shelf.append_book(Book('BLEACH 1'))
book_shelf.append_book(Book('BLEACH 2'))
book_shelf.append_book(Book('BLEACH 3'))
book_shelf.append_book(Book('BLEACH 4'))
book_shelf.append_book(Book('BLEACH 5'))
book_shelf.append_book(Book('BLEACH 6'))


for book in book_shelf:
    print(book.get_name())
