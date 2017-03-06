import turtle
import math


wn=turtle.Screen()

gary = turtle.Turtle()
gary.shape('square')
turtle.tracer(0)
x=-1
y=-10.26
wn.setworldcoordinates(0.1,-10,9.4,10)
for i in range(1200):
    gary.pu()
    x=x+.01
    y=(math.cos(x))*4
    gary.goto(x,y)
    gary.stamp()
gary.goto(0,0)
gary.fillcolor('white')
gary.pencolor('white')
gary.stamp()
