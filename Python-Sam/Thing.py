##Sprite
##Sam Luther
##10/14/16


import turtle
turtle.tracer(0)
gary = turtle.Turtle()
legnum = int(input("input number of legs: "))
leglen = int(input("input length of legs: "))


def drawSprite(gary,legnum,leglen):
    gary.shape('circle')
    gary.shapesize(4)
    gary.stamp()
    dist = 360/legnum
    for i in range(legnum):
        gary.shape('triangle')
        gary.shapesize(.2)
        gary.right(dist-90)
        gary.forward(leglen)
        gary.stamp()
        gary.forward(-leglen)
        gary.right(dist+90)
    gary.shape('circle')
    gary.shapesize(.2)
    gary.forward(13)
    gary.color('thistle1')
    gary.stamp()
    gary.color('gray1')
    gary.shapesize(.05)
    gary.stamp()
    gary.pu()
    gary.forward(-13)
    gary.right(60)
    gary.forward(13)
    gary.pd()
    gary.shapesize(.2)
    gary.color('thistle1')
    gary.stamp()
    gary.color('gray1')
    gary.shapesize(.05)
    gary.stamp()

    
    
        
    
drawSprite(gary,legnum,leglen)
    
