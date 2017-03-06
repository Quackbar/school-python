##Sam Luther
##Tree.py
##Branch width change and color change
##
import turtle
turtle.colormode(255)

def tree(branchLen,t):
    t.pensize(branchLen/5)
    if branchLen > 5:
        t.pencolor(int(branchLen),int(branchLen/5),int(branchLen/5))
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
turtle.hideturtle()
