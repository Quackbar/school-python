#FiveofSatansTurtle
#Sam Luther
#9/13/16
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
import turtle


bgcolor = input("Please Enter a valid color for your background:")
str(bgcolor)
fgcolor = input("Please Enter a valid color for your foreground:")
str(fgcolor)
pensize = input("Please Enter a valid amount for your pensize(1-100):")
int(pensize)
wn=turtle.Screen()
wn.bgcolor(bgcolor)
turing = turtle.Turtle()
x=360
y=144

for i in range(5):
    turing.pd()
    for i in range(5):
        turing.shape("turtle")
        turing.pencolor(fgcolor)
        turing.pensize(pensize)
        turing.forward(60)
        turing.left(216)
    turing.pu()
    turing.forward(360)
    turing.right(144)
turing.hideturtle()
