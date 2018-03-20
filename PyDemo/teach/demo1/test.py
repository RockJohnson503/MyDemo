# encoding: utf-8

"""
File: test.py
Author: Rock Johnson
"""
from teach.demo1.game import Game

if __name__ == '__main__':
    game = Game()

    while True:
        n = input("请输入: ")
        if game.play(int(n)):
            break
    pass