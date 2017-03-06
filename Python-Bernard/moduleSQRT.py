import turtle
import math

i=1000

while(i>0):
    i = (math.sqrt(i)+i)/2
    turtle.forward(i)
    turtle.right(90)
    print(i)
