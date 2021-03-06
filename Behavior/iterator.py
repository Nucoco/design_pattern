# Aim: Search for a certain element from a specific set of elements and return it one by one.
# Constitution: Iterator, ConcreteIterator, Aggregate, ConcreteAggregate

from abc import ABC, abstractmethod


class Book:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# Aggregate
class Aggregate(ABC):

    @abstractmethod
    def iterator(self):
        pass


# ConcreteAggregate
class BookShelf(Aggregate):

    def __init__(self):
        self.__books = []

    def append_book(self, book: Book):
        self.__books.append(book)

    def get_book_at(self, index):
        return self.__books[index]

    def iterator(self):
        return BookShelfIterator(self)

    def __len__(self):
        return len(self.__books)


# Iterator
class Iterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# ConcreteIterator
class BookShelfIterator(Iterator):

    def __init__(self, book_shelf: BookShelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        if self.__index < len(self.__book_shelf):
            return True
        else:
            return False

    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


book_shelf = BookShelf()
book_shelf.append_book(Book('BLEACH 1'))
book_shelf.append_book(Book('BLEACH 2'))
book_shelf.append_book(Book('BLEACH 3'))
book_shelf.append_book(Book('BLEACH 4'))
book_shelf.append_book(Book('BLEACH 5'))
book_shelf.append_book(Book('BLEACH 6'))


book_iterator = book_shelf.iterator()
while(book_iterator.has_next()):
    book = book_iterator.next()
    print(book.get_name())
