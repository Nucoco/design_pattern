# Aim: To present Tree constructure
# Constitution: Component, Composite, Leaf

from abc import ABC, abstractmethod, abstractproperty


# Component
class Component(ABC):

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def size(self):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def print_list(self, path):
        pass

    def __str__(self):
        return f'{self.name} ({self.size})'


# Leaf
class File(Component):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size
        self._parent = None

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    def print_list(self, path=""):
        print(path + '/' + str(self))


# Composite
class Directory(Component):

    def __init__(self, name):
        self.__name = name
        self.__children = {}
        self._parent = None

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        file_size = 0
        for child in self.__children:
            file_size += self.__children[child].size
        return file_size

    def add_child(self, child):
        self.__children[child.name] = child
        child.parent = self

    def remove_child(self, child):
        if child.name in self.__children:
            del self.__children[child.name]
            child.parent = None

    def print_list(self, path=''):
        print(path + '/' + str(self))
        for child in self.__children:
            self.__children[child].print_list(path + '/' + self.name)


file1 = File('tmp1.txt', 1000)
file2 = File('tmp2.txt', 2000)
file3 = File('tmp3.txt', 3000)
file4 = File('tmp4.txt', 4000)

root_dir = Directory('root')
home_dir = Directory('home')
sys_dir = Directory('sys')
my_dir = Directory('my')


root_dir.add_child(home_dir)
root_dir.add_child(sys_dir)

home_dir.add_child(my_dir)
my_dir.add_child(file1)
my_dir.add_child(file2)
home_dir.add_child(file3)
sys_dir.add_child(file4)

root_dir.print_list()
