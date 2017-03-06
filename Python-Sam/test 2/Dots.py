##Sam Luther
##Dots.py
##12/7/16

import turtle
from random import randint
dotSize=0
dotColor='black'

def getDotNum():
    dotNum = input('Number of dots: ')
    return int(dotNum)
def getDotInfoSize():
    dotSize = input('Dot size: ')
    return int(dotSize)
def getDotInfoColor():
    dotColor = input('Dot color: ')
    return dotColor      
def moveTurtle(turt):
    turt.pu()
    x=randint(-350,350)
    y=randint(-350,350)
    turt.goto(x,y)
    turt.pd()
def drawDot(turt,size,color):
    moveTurtle(turt)
    turt.pencolor(color)
    turtle.begin_fill()
    turt.fillcolor(color)
    turt.circle(size)
    turtle.end_fill()
    turtle.hideturtle()

for i in range(getDotNum()):
    drawDot(turtle,getDotInfoSize(),getDotInfoColor())
