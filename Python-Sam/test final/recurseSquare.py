import turtle

def shrinkingSquare(turtle,sideLength,x,y,sub):
    turtle.pu()
    turtle.goto(x+(sub/2),y-(sub/2))
    turtle.pd()
    for i in range(4):
        turtle.forward(sideLength-sub)
        turtle.right(90)
    sub=sub+20
    shrinkingSquare(turtle,sideLength,x,y,sub)
shrinkingSquare(turtle,100,0,0,0)
