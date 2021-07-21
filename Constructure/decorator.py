# Aim: Combine multiple functions into a single Class
# Constitution: Component, ConcreteComponent, Decorator, ConcreteDecorator

from abc import ABC, abstractmethod


# Component
class Component(ABC):

    @abstractmethod
    def operations(self):
        pass


# Concrete Component
class ShowCharComponent(Component):

    def __init__(self, char):
        self.__char = char

    def operations(self):
        print(self.__char * 20)


# Decorator
class ShowDecorator(Component):

    def __init__(self, component: Component):
        self._component = component


class WriteDecorator(Component):

    def __init__(self, component: Component, filename, msg):
        self._component = component
        self._filename = filename
        self._msg = msg


# Concrete Decorator
class ShowMessage(ShowDecorator):

    def __init__(self, component: Component, msg):
        super().__init__(component)
        self.__msg = msg

    def operations(self):
        self._component.operations()
        print(self.__msg)
        self._component.operations()


class WriteMessage(WriteDecorator):

    def operations(self):
        self._component.operations()
        with open(self._filename, 'w') as fh:
            fh.write(self._msg)


show_component = ShowCharComponent('-')
show_message = ShowMessage(show_component, 'Hello world')
# show_message.operations()

write_message = WriteMessage(show_message, 'tmp.txt', 'write message')
write_message.operations()
