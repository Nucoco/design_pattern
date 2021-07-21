# Aim: Notification
# Constitution: Subject, ConcreteSubject, Observer, ConcreteObserver

from abc import ABC, abstractmethod
from random import randint


# Subject
class Subject(ABC):

    def __init__(self):
        self._number = 0
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def execute(self):
        pass


# Concrete Subject
class NumberSubject(Subject):

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def change_value(self):
        number = self._number
        self._number = randint(0, 20)
        print(f'number change from {number} to {self._number}')
        self.notify()

    def execute(self):
        print('Number Subject called')


# Observer
class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


# Concrete Observer
class GraphObserver(Observer):

    def update(self, subject: Subject):
        print('GraphObserver: ' + '*' * subject._number)
        subject.execute()


class NumberObserver(Observer):

    def update(self, subject: Subject):
        print('Number Observer: ' + str(subject._number))
        subject.execute()


subject = NumberSubject()

graph_observer = GraphObserver()
number_observer = NumberObserver()

subject.attach(graph_observer)
subject.attach(number_observer)
subject.change_value()

print('-' * 20)

subject.detach(graph_observer)
subject.change_value()
