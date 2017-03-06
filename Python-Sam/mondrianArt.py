# MondrianArt
##Sam Luther
##22 September 2016

import turtle
import random


turtle.shape('turtle')
screen=turtle.Screen()
screen.setup(940,780)
turtle.bgcolor('black')
turtle.shape("turtle")
turtle.pencolor("dark turquoise")
turtle.fillcolor("light cyan")
turtle.speed(0)
rectNum = int(input('Please enter amount of rectangles: '))
rectWid = int(input('Please enter max width of rectangle: '))
rectWid = max(rectWid,10)
rectHeight = int(input('Please enter max height of rectangle: '))
rectHeight = max(rectHeight,10)

def drawRect(width,height):
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def randColor():
    r=random.randint(0,155)
    g=random.randint(0,255)   
    b=random.randint(0,255)   
    return r,g,b


for i in range(rectNum):
    width = random.randint(5,rectWid)
    height = random.randint(5,rectHeight)
    xaxis = random.randint(-450,400)
    yaxis = random.randint(-383,383)
    turtle.colormode(255)
    turtle.fillcolor(randColor())
    turtle.pencolor('black') 
    turtle.pu()
    turtle.goto(xaxis,yaxis)
    turtle.pd()
    turtle.setheading(0)
    drawRect(width,height)
turtle.hideturtle()

    

