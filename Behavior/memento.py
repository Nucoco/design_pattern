# Aim: Enable to undo
# Constitution: Originator, Memento, ConcreteMemento, CareTaker

from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

import os
import pickle


# Originator
class Originator:

    def __init__(self, state, name):
        self._state = state
        self._name = name

    def change_state(self, new_state):
        print(f'Change state executed: {new_state}')
        self._state = new_state

    def change_name(self, new_name):
        print(f'Change name executed: {new_name}')
        self._name = new_name

    def __str__(self):
        return f'State: {self._state}, name: {self._name}'

    def save(self):
        return ConcreteMemento(self._state, self._name)

    def restore(self, memento):
        self._state = memento.state
        self._name = memento.name
        print(f'Originator: State Change to: {self._state}')


# Memento
class Memento(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractproperty
    def date(self):
        pass


# ConcreteMemento
class ConcreteMemento(Memento):

    def __init__(self, state, name):
        self._state = state
        self._name = name
        self._date = datetime.now()

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    def get_name(self):
        return f'{self.date} / ({self.state})'


# CareTaker
class CareTaker:

    def __init__(self):
        self._mementos = []

    def backup(self, memento: Memento):
        print(f'Stored Originator State: {memento.get_name()}')
        self._mementos.append(memento)

    def undo(self):
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        return memento

    def show_history(self):
        print('Change history')
        for memento in self._mementos:
            print(memento.get_name())


# additional function
class OriginatorBackup:

    @staticmethod
    def dump_file(originator, filename):
        with open(os.path.dirname(__file__) + '/' + filename, 'wb') as fh:
            pickle.dump(originator, fh)

    @staticmethod
    def load_file(filename):
        with open(os.path.dirname(__file__) + '/' + filename, 'rb') as fh:
            return pickle.load(fh)


originator = Originator('FirstState', 'FirstName')
care_taker = CareTaker()

backup_instance = originator.save()
care_taker.backup(backup_instance)

originator.change_state('SecondState')
originator.change_name('SecondName')

backup_instance = originator.save()
care_taker.backup(backup_instance)

# change history
care_taker.show_history()

originator.change_state('ThirdState')
originator.change_name('ThirdName')
# current state
print(originator)
# undo
undo_instance = care_taker.undo()
originator.restore(undo_instance)
# current state
print(originator)

# OriginatorBackup.dump_file(originator, 'tmp.dump')
# originator_2 = OriginatorBackup.load_file('tmp.dump')
# print(originator_2)
# print(type(originator_2))
