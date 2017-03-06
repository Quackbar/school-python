##Sam Luther
##ParLines


import turtle

gary=turtle.Turtle()
y=0
def drawLine(gary,y):
    for i in range(3):
        gary.pd()
        gary.forward(100)
        gary.pu()
        y=y-20
        gary.goto(0,y)
        


drawLine(gary,y)
