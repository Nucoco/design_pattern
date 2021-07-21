# Aim: Remain flexibility to expantion by expressing a state as a class. This lets conditional branches easy.
# Constitution: State, ConcreteState, Context

import io
import os

from abc import ABC, abstractmethod
from datetime import datetime

# State


class State(ABC):

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def end(self):
        pass


# Concrete state
class DayState(State):

    def begin(self):
        print('If state is day then this is called.')

    def write_log(self):
        fh = io.StringIO()
        # with open(f'{os.path.dirname(__file__)}/tmp.txt', 'w', encoding='utf-8') as fh:
        fh.write('Day log')

    def end(self):
        print('End of Day')


class NightState(State):

    def begin(self):
        print('If state is night then this is called.')

    def write_log(self):
        fh = io.StringIO()
        # with open(f'{os.path.dirname(__file__)}/tmp.txt', 'w', encoding='utf-8') as fh:
        fh.write('Night log')

    def end(self):
        print('End of Night')


# Context
class Context:

    def __init__(self):
        self.__state = DayState()

    def do(self):
        self.change_state_by_time()
        self.__state.begin()
        self.__state.write_log()
        self.__state.end()

    def change_state(self, state: State):
        self.__state = state

    def change_state_by_time(self):
        now = datetime.now()
        if (now.hour < 6) or (now.hour >= 19):
            self.__state = NightState()
        else:
            self.__state = DayState()


context = Context()
# context.change_state(NightState())
context.do()
