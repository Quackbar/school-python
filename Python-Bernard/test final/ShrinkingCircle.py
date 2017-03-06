import turtle
import random

##turtle.colormode(255)
turtle.speed(0)

colors = ['red2','dark orange','yellow','green2','blue','purple3','purple4','MediumPurple1','deep pink']

def shrinkingCircles(t,radius,x,y,i,backNum):
    t.pu()
##    r=random.randint(1,255)
##    g=random.randint(1,255)
##    b=random.randint(1,255)
    t.fillcolor(colors[i])
    t.goto(x,y)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    i=i+1
    radius=radius-30
    y=y+30
    if(i==backNum):#radius > 5 and radius <= 275):
        i=0
    if(radius<=5):
        print('',end='')
    else:
        shrinkingCircles(t,radius,x,y,i,backNum)
##        radius=radius-30  
##        y=y+30
##    else:
##        shrinkingCircles(turtle,275,0,-275,0,8)

shrinkingCircles(turtle,275,0,-275,0,8)
turtle.hideturtle()
