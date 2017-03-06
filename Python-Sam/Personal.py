import turtle
from random import randint
import math

screen = turtle.Screen()
screen.setup(1000, 70)
move_speed = 10
turn_speed = 10

i=1


enemTurtList1 = ['1','2','3','4','5','6']
def up():
    turtle.left(90)
    turtle.forward(move_speed)
    turtle.right(90)
def down():
    turtle.right(90)
    turtle.forward(move_speed)
    turtle.left(90)
def left():
  turtle.backward(move_speed)

def right():
  turtle.forward(move_speed)

turtle.penup()
turtle.speed(0)
turtle.goto(-480,0)

screen.listen()

screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")



while(i>0):

    for i in range(4):
        e=100
        enemTurtList1[i]=turtle.Turtle()
        enemTurtList1[i].pu()
        enemTurtList1[i].ht()       
        enemTurtList1[i].speed(100)
        enemTurtList1[i].goto(490,(randint(-1,2))*10)
        enemTurtList1[i].speed(1)
        enemTurtList1[i].st()
        enemTurtList1[i+1]=turtle.Turtle()
        enemTurtList1[i+1].pu()
        enemTurtList1[i+1].ht()       
        enemTurtList1[i+1].speed(1)
        enemTurtList1[i+1].goto(490,(randint(-1,2))*10)
        enemTurtList1[i+1].speed(1)
        enemTurtList1[i+1].st()
        enemTurtList1[i+2]=turtle.Turtle()
        enemTurtList1[i+2].pu()
        enemTurtList1[i+2].ht()       
        enemTurtList1[i+2].speed(100)
        enemTurtList1[i+2].goto(490,(randint(-1,2))*10)
        enemTurtList1[i+2].speed(1)
        enemTurtList1[i+2].st()
        while(e>0):
            e=e-1
            enemTurtList1[i].backward(10)
            enemTurtList1[i+1].backward(10)
            enemTurtList1[i+2].backward(10)
            if(enemTurtList1[i].xcor()==turtle.xcor() or enemTurtList1[i+1].xcor()==turtle.xcor()or enemTurtList1[i+2].xcor()==turtle.xcor() and enemTurtList1[i].ycor()==turtle.ycor() or enemTurtList1[i+1].ycor()==turtle.ycor()or enemTurtList1[i+2].ycor()==turtle.ycor() or turtle.ycor()<-10 or turtle.ycor()>20):
                print('u dead')
            if(turtle.xcor()>480):
                print('u won')




