# encoding: utf-8

"""
File: person.py
Author: Rock Johnson
"""
class Person:
    def __init__(self, name):
        self._name = name

    def show(self):
        print('装扮的%s' % self._name)