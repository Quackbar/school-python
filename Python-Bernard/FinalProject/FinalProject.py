import turtle
import random
import gtk
import threading
import mtTkinter as Tkinter
import thread
import time

travelerSpeed = 0
while travelerSpeed > 10 or travelerSpeed < 1:
    travelerSpeed = input("Enter the difficulty(1-10): ")

#Turtle Settings
wn = turtle.Screen()
falcon = "/home/bernardk/Code/Python/FinalProject/ship.gif"
falconR = "/home/bernardk/Code/Python/FinalProject/shipR.gif"
falconL = "/home/bernardk/Code/Python/FinalProject/shipL.gif"
falconD = "/home/bernardk/Code/Python/FinalProject/shipD.gif"
wn.addshape(falcon)
turt = turtle.Turtle()
turtle.bgcolor("black")
turt.pu()
turt.shape(falcon)
turt.fillcolor("snow")
turt.goto(0, 0)

#Screen Setup
window = gtk.Window()
screen = window.get_screen()
width = screen.get_width()
height = screen.get_height()
wn.screensize()
wn.setup(width=1.0, height=1.0)


#Key Action Handelers
def up():
    global falcon
    print("up")
    turt.setheading(90)
    #turt.shape(falcon)
    evilMove()
    turt.forward(2)

def left():
    global falconL
    print("Left")
    turt.setheading(180)
    #turt.shape(falconL)
    evilMove()
    turt.forward(2)

def right():
    global falconR
    print("Right")
    turt.setheading(0)
    #turt.shape(falconR)
    evilMove()
    turt.forward(2)

def down():
    global falconD
    print("Down")
    turt.setheading(270)
    #turt.shape(falconD)
    evilMove()
    turt.forward(2)



#Supports on the Bottom
builder = turtle.Turtle()
builder.tracer(0)
builder.pencolor("snow")
builder.fillcolor("snow")
builder.ht()
startx = -width/2
starty = (-height/2) + 100
blockWidth = width/10
blockHeight = 50

def buildBlock(num, fill):
    builder.pu()
    builder.goto(startx + (blockWidth*num), starty)
    builder.pd()
    if fill:
        builder.begin_fill()
    builder.setheading(0)
    for i in range(2):
        builder.forward(blockWidth)
        builder.right(90)
        builder.forward(blockHeight)
        builder.right(90)

    if fill:
        builder.end_fill()

for i in range(10):
    buildBlock(i, False)

#Make the helpless traveler
traveler = turtle.Turtle()
traveler.pu()
traveler.pensize(2)
traveler.goto(-width/2, (-height/2) + 25)
traveler.setheading(0)
traveler.pencolor("navy")
traveler.pd()
traveler.pensize(3)

#Laser Colors
colors = ["blue2", "green2", "red", "purple3", "snow", "yellow2"]

#Declare Nice Guy
nice = turtle.Turtle()
nice.shape("circle")
nice.fillcolor("cyan")
nice.pencolor("cyan")
nice.pu()
nice.goto(random.randint((-width / 2) + 20, (width / 2) - 20), random.randint((-height/2) + 120, (height / 2) - 20))

#Declare Evil Entities
e0 = turtle.Turtle()
e1 = turtle.Turtle()
e2 = turtle.Turtle()
e3 = turtle.Turtle()
e4 = turtle.Turtle()
e5 = turtle.Turtle()
e6 = turtle.Turtle()
e7 = turtle.Turtle()
e8 = turtle.Turtle()
e9 = turtle.Turtle()
e10 = turtle.Turtle()
e12 = turtle.Turtle()
e13 = turtle.Turtle()
e14 = turtle.Turtle()
e15 = turtle.Turtle()
e16 = turtle.Turtle()
e17 = turtle.Turtle()
e18 = turtle.Turtle()
e19 = turtle.Turtle()
e20 = turtle.Turtle()
e21 = turtle.Turtle()
e22 = turtle.Turtle()
e23 = turtle.Turtle()
e24 = turtle.Turtle()
e25 = turtle.Turtle()
e26 = turtle.Turtle()
e27 = turtle.Turtle()
e28 = turtle.Turtle()
e29 = turtle.Turtle()
e30 = turtle.Turtle()
e31 = turtle.Turtle()
e32 = turtle.Turtle()
e33 = turtle.Turtle()
e34 = turtle.Turtle()
e35 = turtle.Turtle()
e36 = turtle.Turtle()
e37 = turtle.Turtle()
e38 = turtle.Turtle()
e39 = turtle.Turtle()
e40 = turtle.Turtle()
e41 = turtle.Turtle()
e42 = turtle.Turtle()
e43 = turtle.Turtle()
e44 = turtle.Turtle()
e45 = turtle.Turtle()
e46 = turtle.Turtle()
e47 = turtle.Turtle()
e48 = turtle.Turtle()
e49 = turtle.Turtle()

evil = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42, e43, e44, e45, e46, e47, e48, e49,]
speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
difficulty = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

def evilReset(i, first):
    if difficulty[i] < 10:
        difficulty[i] += 1
    evil[i].tracer(0)
    if first:
        evil[i].goto(random.randint(-(width / 2), (width / 2)), random.randint((height / 2), (height * 1.5)))
    else:
        evil[i].goto(random.randint(-(width / 2), (width / 2)), random.randint((height / 2), (height/2 + 30)))
    evil[i].tracer(1)
    speed[i] = random.randint(5, difficulty[i])
    evil[i].fillcolor(colors[random.randint(0, 5)])
    evil[i].setheading(270)

for i in range(0, len(evil), 1):
    evil[i].pu()
    evilReset(i, True)


wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(down, "Down")
wn.listen()
#turtle.mainloop()


def collide(turt1, turt2):
    if turt1.xcor() - turt2.xcor() < 10:
        if turt.ycor() - nice.ycor() < 10:
            return True
        else:
            return False
    else:
        return False

alive = True
success = False
blockNum = -1

def falconMove():
    time.sleep(.1)
    print("FALCON MOVE")
    global wn
   # while True:
    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(down, "Down")

def evilMoveTotal():
    print("Evil move")
    global alive
    global success
    global blockNum
    global traveler
    global travelerSpeed

    traveler.forward(travelerSpeed)
  #  while True:
    for i in range(0, len(evil), 1):
        #evil[i].tracer(0)
        evil[i].forward(speed[i] + (travelerSpeed * 2))
        for j in range(0, len(evil), 1):
            if collide(turt, evil[j]):
                alive = False
                success = False
            if collide(traveler, evil[j]):
                alive = False
                success = False
        if evil[i].ycor() < -(height / 2):
            evilReset(i, False)
        if collide(turt, nice):
            blockNum += 1
            nice.goto(random.randint(-(width / 2) + 20, (width / 2) - 20),
                      random.randint(-(height / 2) + 120, (height / 2) - 20))
            buildBlock(blockNum, True)
        if blockNum == 9 or traveler.xcor() > width / 2:
            success = True
            alive = False
        #evil[i].tracer(1)

def evilMove():
    global travelerSpeed
    traveler.forward(travelerSpeed)
    for i in range(0, len(evil), 1):
        evil[i].tracer(0)
        evil[i].forward(speed[i])

while alive:
    print("loop through while alive")
    evilMoveTotal()
    falconMove()



if success:
    exit()
    print("Congrats you Won")
else:
    exit()
    print("You suck better luck next time")

print("The End")