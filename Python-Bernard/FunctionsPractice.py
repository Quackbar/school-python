##Function Practice
##Sam Luther
##10/6/16
##This is an in class practice
##focusing on functions
##_________      ______________________
##\_____  |      |  __________________/
##    \ | |      | | /
##     \| |______| |/
##     /            \
##    |--||||-||||---|
##    |  \||/ \||/   |
##     |     oo     |
##      \___/\/\___/
##         |____|
##        /      \
##       /        \
##      /          \
##     /  |      |  \
##    |   |      |   |
##    |   |      |   |
##    /___\______/___\
##       |        |       (\ /)
##       |   __   |       (^_^)
##      /____\/____\      C(")(")



##------------------------------##
##        From Buffy            ##
##------------------------------##


import turtle, random

turtle.tracer(0)

sidelength = int(input("input length of side: "))


squareturtle = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("magenta3")
y=200


##--------------------------------------------------------------------------##
##      Takes one argument(a turtle & length) and it is non-fruitful        ##
##--------------------------------------------------------------------------##

def drawSquare(gary, length):

    gary.pencolor(randomcolor())

#Calls a Function from a Function {
    gary.fillcolor(randomcolor())
#}
    gary.begin_fill()
    
    for i in range(4):
        gary.forward(length)
        gary.right(90)

    gary.end_fill()

def moveturtle(gary,x,y):
    gary.pu()
    gary.goto(x,y)
    gary.pd()
##-------------------------------------------------------------------##
##          Fruitful with no arguments  && Color Stuff               ##
##-------------------------------------------------------------------##

wn.colormode(255)


def randomcolor():
#generates random values for color {
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    print('red'+str(red)+'blue'+str(blue)+'green'+str(green)+'')
#}    
    return (red,green,blue)


##------------------------------------------------------------##
##                  Function call: Draw Once                  ##
##------------------------------------------------------------##

drawSquare(squareturtle,sidelength)


##------------------------------------------------------------##
##                  Function call: Draw Twice                 ##
##------------------------------------------------------------##

moveturtle(squareturtle,-150,-150)
drawSquare(squareturtle,sidelength/2)


##------------------------------------------------------------##
##                  Grid of randcol squares                   ##
##------------------------------------------------------------##

moveturtle(squareturtle,-200,y)

for column in range(10):
    for row in range(10):
        drawSquare(squareturtle,10)
        squareturtle.forward(10)
    y=y-10
    moveturtle(squareturtle,-200,y)









