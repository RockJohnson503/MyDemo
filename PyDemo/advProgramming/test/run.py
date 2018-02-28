# encoding: utf-8

"""
File: run.py
Author: Rock Johnson
"""
import datetime
import numpy as np
import random as rd

def test():
    evens = [i for i in range(10) if i % 2 == 0]
    return evens

playerScore = 0
machineScore = 0
count = 0
def play():
    rules = {"石头": "剪刀", "剪刀": "布", "布": "石头"}
    machineRules = np.array(["石头", "剪刀", "布"])
    player = input("玩家请输入:")
    if player not in rules:
        print("请正确输入")
        play()
    machine = np.random.choice(machineRules)
    print("玩家：" + player + ", 人机：" + machine)
    if rules[player] == machine:
        print("玩家胜利")
        global playerScore
        playerScore += 1
    elif rules[machine] == player:
        print("人机胜利")
        global machineScore
        machineScore += 1
    else:
        print("平局")
    global count
    count += 1
    again = input("是否继续(Y/Other):")
    if again == "Y" or again == "y":
        play()
    else:
        print("您一共玩了" + str(count) + "局, 玩家得分：" + str(playerScore) + ", 人机得分：" + str(machineScore) + ", 平局：" + str(count-machineScore-playerScore) + "次.")

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def psychologist():
    print("Please tell me your problems")
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Dont't ask yourself too much questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Dont't be so negative")
            elif '傻逼' in answer:
                print("你才是傻逼")
            elif 'what\'s your name' in answer:
                print("Please call me baby")
            else:
                print("Sorry, I don't understand")

if __name__ == '__main__':
    # with open('/home/rock/文档/激活码') as lines:
    #     for line in lines:
    #         if line.startswith("#"):
    #             continue
    #         else:
    #             print(line.strip())
    print(rd.randint(0, 10))
    pass