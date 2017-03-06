#Minecraft
#Sam Luther
#9/26/16
#This program makes a minecraft block
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
#randint(0,180)
#21x21 46pixels x 38pixels
from random import randint
import turtle
wn=turtle.Screen()
wn.bgcolor("lightblue1")
turtle.shape("square")
turtle.speed(0)
turtle.tracer(0)
x=-50
y=50
xx=0
yy=0
rowc=0
turtle.shapesize(0.05,0.005)
turtle.pu()
turtle.goto(x+xx,y+yy)
colorG = 0
rowC=0
j=3
r=0
colorListG = ['darkgreen', 'seagreen', 'forestgreen', 'yellowgreen', 'mediumseagreen', 'green2','green3','green4','OliveDrab1','OliveDrab2','OliveDrab4']
colorListB = ['saddlebrown', 'salmon4', 'brown4', 'LightSalmon4', 'OrangeRed4', 'gray2', 'seashell3','lightblue2']
colorListBoth = ['saddlebrown', 'salmon4', 'brown4', 'LightSalmon4','darkgreen', 'seagreen', 'forestgreen', 'yellowgreen', 'mediumseagreen', 'green2','green3','green4','OliveDrab1','OliveDrab2','OliveDrab4']
colorListBum = ['saddlebrown', 'salmon4', 'lightblue2', 'LightSalmon4', 'OrangeRed4', 'gray2', 'yellowgreen','brown4']
colorListS = ['snow','gray99','gray2','gray35','gray98','gray3','gray1',]
app=0
while(j>0):
    for i in range(10000):

        if(rowC<=12):
            colorG = randint(0,5)
            turtleColor = colorListG[colorG]
            turtle.color(turtleColor)
            x=x+1
            rowc = rowc+1
            turtle.goto(x+xx,y+yy)
            turtle.pd()
            turtle.stamp()
            turtle.pu()
        if(rowC>12 and rowC<=18):
            colorG = randint(0,9)
            turtleColor = colorListBoth[colorG]
            turtle.color(turtleColor)
            x=x+1
            rowc = rowc+1
            turtle.goto(x+xx,y+yy)
            turtle.pd()
            turtle.stamp()
            turtle.pu()
        if(rowC>18 and rowC<=30):
            colorG = randint(0,7)
            turtleColor = colorListBum[colorG]
            turtle.color(turtleColor)
            x=x+1
            rowc = rowc+1
            turtle.goto(x+xx,y+yy)
            turtle.pd()
            turtle.stamp()
            turtle.pu()   
        if(rowC>30):
            colorG = randint(0,6)
            turtleColor = colorListB[colorG]
            turtle.color(turtleColor)
            x=x+1
            rowc = rowc+1
            turtle.goto(x+xx,y+yy)
            turtle.pd()
            turtle.stamp()
            turtle.pu()          
        if(app==1):
            colorG = randint(0,3)
            turtleColor = colorListS[colorG]
            turtle.color(turtleColor)
            x=x+1
            rowc = rowc+1
            turtle.goto(x+xx,y+yy)
            turtle.pd()
            turtle.stamp()
            turtle.pu()
        if(rowc==100):
            y=y-1
            x=x-100
            rowc=0
            rowC=rowC+1
            print(str(rowC))
    r=r+1
    if(j==3):
        j=j-1
        xx=xx+100
        y=50
        rowC=0
        rowc=0
        if(r==2):
            xx=xx-100
            yy=yy-100
            r=0
##        858
    if(j==2):
        j=j-1
        xx=xx+100        
        y=50
        rowc=0
        if(r==2):
            xx=xx-100
            yy=yy-100
            r=0
    if(j==1):
        app=1
        j=j-1
        xx=xx+100        
        y=50
        rowc=0
        if(r==2):
            xx=xx-100
            yy=yy-100
            r=0        

