##Sam Luther
##WriteMessage.py
##12/8/16


import turtle

wn = turtle.Screen()

        
def moveTurtle(turt):
    turt.pu()
    x = input('X coordinate: ')
    y = input('Y coordinate: ')
    turt.goto(int(x),int(y))
    turt.pd()
def writeMessage(turt,message,color1,color2,fontName,fontSize):
    x=1
    messageL = list(message)
    for i in range(len(message)):
        if(x==1):
            turtle.pencolor(color1)
            x=0
        elif(x==0):
            turtle.pencolor(color2)
            x=1
        turtle.forward(int(fontSize))
        turtle.write(messageL[i], False, align="center",font = (fontName,fontSize,'normal'))
        
def getInput():
    bgC = input('Background Color: ')
    message = input('Message: ')
    fontName = input('Font: ')
    fontSize = input('Font Size: ')
    color1 = input('First Color: ')
    color2 = input('Second Color: ')
    wn.bgcolor(bgC)
    moveTurtle(turtle)
    writeMessage(turtle,message,color1,color2,fontName,fontSize)
    


getInput()
turtle.hideturtle()
