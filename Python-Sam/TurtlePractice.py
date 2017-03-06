import turtle
from random import randint

wn=turtle.Screen()
wn.bgcolor("magenta3")
i=1
##while(i==1):
##    turtle.shape("turtle")
##    turtle.speed(1)
##    turtle.pencolor("peach puff")
##    turtle.fillcolor("SkyBlue1")
##    turtle.begin_fill()
##    turtle.forward(120)
##    turtle.right(randint(0,180))
##    turtle.forward(120)
##    turtle.right(randint(0,180))
##    turtle.forward(120)
##    turtle.right(randint(0,180))
##    turtle.forward(120)
##    turtle.right(randint(0,180))
##    turtle.end_fill()

turtle.pu()
turtle.goto(-150,200)
turtle.pd()
turtle.pensize(100)
turtle.pencolor("salmon")
turtle.fillcolor("light slate blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.pencolor("salmon")
turtle.pu()
turtle.goto(-150,-200)
turtle.pd()
turtle.stamp()

turtle.pu()
turtle.goto(-150,-250)
turtle.pd()
turtle.stamp()


turtle.pu()
turtle.goto(-150,-150)
turtle.pd()
turtle.stamp()


turtle.pu()
turtle.goto(-150,-300)
turtle.pd()
turtle.stamp()

turtle.pu()
turtle.home()
turtle.pd()
turtle.shapesize(5,5)
