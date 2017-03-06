##Sam Luther
##onClickRandTurn.py
##12/7/16

import turtle
import random

runner = turtle.Turtle()
turnList = [0,60,120,180,240,300]
def move(x,y):
    direction = random.randint(0,5)
    runner.left(turnList[direction])
    runner.forward(50)
turtle.onscreenclick(move)
