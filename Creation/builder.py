# Builder pattern
from abc import ABC, abstractmethod, abstractproperty


# Product
class SetMeal:

    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self):
        return f'MainDish: {self.main_dish}, SideDish: {self.side_dish}'


# Builder Interface
class SetMealBuilder(ABC):

    def __init__(self):
        self._set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def build_main_dish(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass


# Concrete Builder
class SanmaSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'Sanma'

    def build_side_dish(self):
        self._set_meal.side_dish = 'MisoSoup'


class PastaSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'Pasta'

    def build_side_dish(self):
        self._set_meal.side_dish = 'Soup'


# Director
class Director:

    def __init__(self, builder: SetMealBuilder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        self.builder.build_main_dish()
        self.builder.build_side_dish()


# Instantiating
sanma_builder = SanmaSetBuilder()
pasta_builder = PastaSetBuilder()

director = Director(sanma_builder)
director.build()
print(director.builder.product)

director = Director(pasta_builder)
director.build()
print(director.builder.product)
