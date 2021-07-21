# Aim: Provide a simple interface to manupulate a complex system. Like API.
# Constitution: Facade, Others(A - Z)

class Knife:

    def __init__(self, name):
        self.__name = name

    def cut_vegetables(self):
        print(f'Cut a vegetable with {self.__name}')


class Boiler:

    def __init__(self, name):
        self.__name = name

    def boil_vegetables(self):
        print(f'Boil a vegetable with {self.__name}')


class Frier:

    def __init__(self, name):
        self.__name = name

    def fry_vegetables(self):
        print(f'Fry a vegetable with {self.__name}')


# Facade
class Cook:

    def __init__(self, knife: Knife, boiler: Boiler, frier: Frier):
        self.__knife = knife
        self.__boiler = boiler
        self.__frier = frier

    def cook_dish(self):
        self.__knife.cut_vegetables()
        self.__boiler.boil_vegetables()
        self.__frier.fry_vegetables()


knife = Knife('My knife')
boiler = Boiler('My boiler')
frier = Frier('My frier')

cook = Cook(knife, boiler, frier)
cook.cook_dish()
