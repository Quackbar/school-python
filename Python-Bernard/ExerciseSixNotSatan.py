#ExcersiseSixNotSatan
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
sides = input("Please Enter a valid amount for the length of your sides:")
int(sides)
nsides = input("Please Enter a valid amount for the number of sides you would like:")
int(nsides)
asides = input("Please Enter a valid amount for angle you wish each side to turn from the       previous side:")
int(asides)
fillq = input("Would you like the shape to be filled after completion? Please answer fill or no fill:")
str(fillq)
turing = turtle.Turtle()
if(fillq == "fill"):
    fillcq = input("Please enter a valid color to fill the shape with:")
    str(fillcq)
    turing.fillcolor(str(fillcq))
    turing.begin_fill()
    for i in range(int(nsides)):
            wn=turtle.Screen()
            wn.bgcolor(bgcolor)
            

            
            turing.shape("turtle")
            turing.pencolor(fgcolor)
            turing.pensize(pensize)
            turing.forward(int(sides))
            turing.left(int(asides))
    turing.end_fill()
else :
    for i in range(int(nsides)):
            wn=turtle.Screen()
            wn.bgcolor(bgcolor)
            
            turing.shape("turtle")
            turing.pencolor(fgcolor)
            turing.pensize(pensize)
            turing.forward(int(sides))
            turing.left(int(asides))
    
