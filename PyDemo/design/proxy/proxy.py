# encoding: utf-8

"""
File: proxy.py
Author: Rock Johnson
"""
from .givegift import GiveGift
from .pursuit import Pursuit


class Proxy(GiveGift):
    def __init__(self, name, pursuit, girl):
        self._pursuit = Pursuit(pursuit, girl)
        self._name = name

    def give_chocolate(self):
        print(self._name, ':', end=' ')
        self._pursuit.give_chocolate()

    def give_flowers(self):
        print(self._name, ':', end=' ')
        self._pursuit.give_flowers()

    def give_dolls(self):
        print(self._name, ':', end=' ')
        self._pursuit.give_dolls()