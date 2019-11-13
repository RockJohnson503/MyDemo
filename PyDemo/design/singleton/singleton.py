# encoding: utf-8

"""
File: singleton.py
Author: Rock Johnson
"""
import threading


class Singleton:
    def __init__(self, name=None):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def open(self):
        print('打开', self.name)


def task(arg):
    o = Singleton(arg)
    o.open()


if __name__ == '__main__':
    a = Singleton('Rock')
    a.open()
    b = Singleton('Johnson')
    b.open()
    c = Singleton('King')
    c.open()

    for i in range(10):
        t = threading.Thread(target=task, args=[i])
        t.start()