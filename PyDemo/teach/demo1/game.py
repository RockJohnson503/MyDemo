# encoding: utf-8

"""
File: game.py
Author: Rock Johnson
"""
import random

class Game:
    # 游戏

    def __init__(self):
        self.__randomNum = random.randrange(101)
        self.__count = 1

    def play(self, n):
        if n == self.__randomNum:
            print("猜对了, 总共用了: %s次" % self.__count)
            return True
        elif n > self.__randomNum:
            print("比%s小" % n)
        else:
            print("比%s大" % n)
        self.__count += 1
        return False