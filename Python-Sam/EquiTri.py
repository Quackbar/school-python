##EquiTri
##Sam Luther
##10/7/16
import turtle

sidelength = int(input("input length of side: "))
wn = turtle.Screen()
wn.bgcolor("magenta3")
turt = turtle.Turtle()

def drawEquitriangle(gary, length):
    gary.pd()
    
    for i in range(3):
        gary.forward(length)
        gary.right(120)
    

drawEquitriangle(turt, sidelength)
