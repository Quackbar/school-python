#Spiral
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

turing = turtle.Turtle()
length = 30

for i in range(100):
    turing.shape("turtle")
    turing.pensize(1)
    turing.forward(length)
    turing.left(90)
    length = length +10
