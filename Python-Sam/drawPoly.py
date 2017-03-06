import turtle
import random
t = turtle.Turtle()
turtle.colormode(255)

def drawPoly(t,length,sideNum,r,g,b):
    if(sideNum>1):
        r=r+10
        g=g+25
        b=b+35
        t.fillcolor(r,g,b)
        t.begin_fill()
        for i in range(sideNum):
            t.forward(length)
            t.left(360/sideNum)
        t.end_fill()
        sideNum = sideNum-1
        drawPoly(t,length,sideNum,r,g,b)
length = input('please input a side length: ')
sideNum = input('please input a number of sides: ')
r=0
g=0   
b=0
drawPoly(t,int(length),int(sideNum),r,g,b)
