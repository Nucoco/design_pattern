# Factory method
from abc import ABC, abstractmethod, abstractproperty


# Interface Factory( Creator)
class IFactory(ABC):

    def __init__(self):
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product_owner(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product_owner(self, product):
        pass


# Concrete Factory( Concrete Creator)
class CarFactory(IFactory):

    def _create_product(self):
        return Car(self._owner)

    def _register_product_owner(self, product):
        self.registered_owners.append(product.owner)


class ShipFactory(IFactory):

    def _create_product(self):
        return Ship(self._owner)

    def _register_product_owner(self, product):
        self.registered_owners.append(product.owner)


# Interface Product
class IProduct(ABC):

    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def owner(self):
        pass


# Concrete Product
class Car(IProduct):

    def use(self):
        print(f'{self.owner}: Drive')

    @property
    def owner(self):
        return self._owner


class Ship(IProduct):

    def use(self):
        print(f'{self.owner}: Ship')

    @property
    def owner(self):
        return self._owner


car_factory = CarFactory()
john_car = car_factory.create('John')
lucy_car = car_factory.create('Lucy')
john_car.use()
lucy_car.use()
print(car_factory.registered_owners)

ship_factory = ShipFactory()
mike_ship = ship_factory.create('Mike')
cake_ship = ship_factory.create('Cake')
mike_ship.use()
cake_ship.use()
print(ship_factory.registered_owners)
