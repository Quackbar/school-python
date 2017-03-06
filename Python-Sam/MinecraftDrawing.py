##Sam Luther
##MinecraftDrawing
##11/3/16

import turtle

gary = turtle.Turtle()
turtle.tracer(0)

color = 'black'
x=1
y=1
gary.pu()

z=0
for i in range(20):
    gary.goto(-200+z,200)
    gary.goto(-200+z,-200)
    z=z+20


def square(color,x,y):
    gary.goto(x,y)
    gary.pencolor(color)
    gary.fillcolor(color)
    gary.begin_fill()
    for i in range(4):
        gary.forward(20)
        gary.right(90)
    gary.end_fill()
    gary.goto(0,0)
def leftrighttri(color,x,y):
    gary.goto(x,y)
    gary.pencolor(color)
    gary.fillcolor(color)
    gary.begin_fill()
    gary.forward(20)
    gary.right(135)
    gary.forward(28.2842712475)
    gary.right(135) 
    gary.forward(20)    
    gary.end_fill()
    gary.goto(0,0)
def rightrighttri(color,x,y):
    gary.goto(x,y)
    gary.pencolor(color)
    gary.fillcolor(color)
    gary.begin_fill()
    gary.forward(20)
    gary.right(90)
    gary.forward(20)
    gary.right(135)
    gary.forward(28.2842712475)
    gary.end_fill()
    gary.goto(0,0)

cat=['black','black','black','gray30','black','black','gray30','black','black','gray30','gray30','black','black','black','gray30','gray30','gray30','black','black','black','black','black','black','gray30','gray30','gray30','gray8','gray30','gray8','gray30','gray30','gray30','gray30','gray8','gray8','gray30','gray8','black','black','black','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','gray8','gray30','gray8','gray8','gray30','black','black','gray30','black','gray30','gray30','black','gray30','gray30','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','black','gray30','gray30','gray30','gray30','black','black','black','gray30','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','gray30','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','black','black','gray8','gray30','black','black','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','gray30','black','gray8','gray30','gray8','gray30','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
caty=[4,10,3,4,5,9,10,11,3,4,5,6,7,8,9,10,11,12,13,14,15,16,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
catx=[0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]
for i in range(233):
    square(cat[i],(-caty[i]*20),(-catx[i]*20))

square('black',-360,-200)
square('black',-360,-220)
square('black',-380,-180)
square('black',-400,-160)
square('black',-400,-140)
leftrighttri('brown4',-200,0)
rightrighttri('brown4',-80,-20)

##leftrighttri('red',20,20)
##leftrighttri('red',-20,-20)


