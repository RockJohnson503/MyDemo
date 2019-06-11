# encoding: utf-8

"""
File: finery.py
Author: Rock Johnson
"""
from .person import Person


class Finery(Person):
    def __init__(self):
        Person.__init__(self, None)

    def decorate(self, component):
        if isinstance(component, Person):
            self._component = component
        else:
            raise TypeError('请装饰人!')

    def show(self):
        if self._component:
            self._component.show()


class TShirts(Finery):
    def show(self):
        print('大T恤', end=' ')
        Finery.show(self)


class BigTrouser(Finery):
    def show(self):
        print('垮裤', end=' ')
        Finery.show(self)


class Sneakers(Finery):
    def show(self):
        print('破球鞋', end=' ')
        Finery.show(self)


class Suit(Finery):
    def show(self):
        print('西装', end=' ')
        Finery.show(self)


class Tie(Finery):
    def show(self):
        print('领带', end=' ')
        Finery.show(self)


class LeatherShoes(Finery):
    def show(self):
        print('皮鞋', end=' ')
        Finery.show(self)