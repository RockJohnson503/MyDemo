# encoding: utf-8

"""
File: pursuit.py
Author: Rock Johnson
"""
from .givegift import GiveGift


class Pursuit(GiveGift):
    def __init__(self, name, girl):
        self._girl = girl
        self._name = name

    def __str__(self):
        return self._name

    def give_dolls(self):
        print(self._girl, '%s送你洋娃娃' % self._name)

    def give_flowers(self):
        print(self._girl, '%s送你鲜花' % self._name)

    def give_chocolate(self):
        print(self._girl, '%s送你巧克力' % self._name)