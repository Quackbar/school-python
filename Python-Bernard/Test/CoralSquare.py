##Sam Luther
##CoralSquare
##TEST
import turtle
wn=turtle.Screen()
wn.bgcolor("black")
x=0
y=0
gary=turtle.Turtle()
def drawSquare(gary,x,y):
    gary.goto(x,y)
    gary.fillcolor("coral")
    gary.begin_fill()
    for i in range(4):
        gary.pd()
        gary.forward(100)
        gary.right(-90)
    gary.end_fill()
    gary.hideturtle()
drawSquare(gary,x,y)
