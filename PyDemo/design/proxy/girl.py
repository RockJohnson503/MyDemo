# encoding: utf-8

"""
File: girl.py
Author: Rock Johnson
"""
class Girl:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name