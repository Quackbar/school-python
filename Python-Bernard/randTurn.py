# -----------------------------------------+
# Sam Luther                               |
# randTurn.py                              |
# Last Updated: November, 16, 2016         |
# -----------------------------------------|
#                                          |
# -----------------------------------------+

turnList = [0,60,120,180,240,300]

import random
from random import randint
import turtle

def moveRandomTri(wn, t):
    i=randint(0,5)
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(turnList[i])
##        t.left(90)
    else:
        t.left(turnList[i])
##        t.right(90)
    t.forward(20)

def moveRandomSquare(wn, t):
    i=randint(0,5)
    coin = random.randrange(0,2)
    if coin == 0:
##        t.left(turnList[i])
        t.left(90)
    else:
##        t.left(turnList[i])
        t.right(90)
    t.forward(20)

def turnAround(wn, t):
    t.left(180)
    t.forward(20)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False
def randColor():
    r=random.randint(0,155)
    g=random.randint(0,255)   
    b=random.randint(0,255)   
    return r,g,b
def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.speed(0)
t2.speed(0)
wn = turtle.Screen()
turtle.colormode(255)




leftBound = -wn.window_width() / 2.1
rightBound = wn.window_width() / 2.1
topBound = wn.window_height() / 2.1
bottomBound = -wn.window_height() / 2.1

t1.up()
t1.goto(-20,0)
t1.down()

t2.up()
t2.goto(20,0)
t2.down()

while(True):
    if ((isInScreen(wn, t1)==False) or (t1.xcor()==t2.xcor() and t1.ycor()==t2.ycor())):
        turnAround(wn, t1)
##        wn.exitonclick()
    elif ((isInScreen(wn, t2)==False) or (t1.xcor()==t2.xcor() and t1.ycor()==t2.ycor())):
        turnAround(wn, t2)
##        wn.exitonclick()
    t1.pencolor(randColor()) 
    moveRandomSquare(wn, t1)
    t2.pencolor(randColor()) 
    moveRandomSquare(wn, t2)
        

wn.exitonclick()
