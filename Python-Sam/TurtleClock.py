#TurtleClock
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
##      /____\/____\      C(")(")\
import turtle
wn=turtle.Screen()
wn.bgcolor("purple1")
turn=0
turtle.shape("turtle")
turtle.pencolor("magenta3")
turtle.fillcolor("magenta3")
turtle.stamp()
for i in range(12):   
    turtle.pu()
    turtle.right(30)
    turtle.forward(200)
    turtle.pd()
    turtle.stamp()
    turtle.pu()
    turtle.forward(-30)
    turtle.pd()
    turtle.forward(-10)
    turtle.pu()
    turtle.goto(0,0)
    turtle.pd()
    turn=turn+30
    
    

