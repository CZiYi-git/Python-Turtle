import turtle
import math
turtle.title("Turtle Example")


t = turtle.Turtle()
t.shape("turtle")
t.speed(999999999999999999999999999999999999999999999999)


# draw a christmas tree
def DrawChristmasTree(a):
    
    trunk_width = 45
    trunk_height = trunk_width*1.5

    for i in range(3):
        b = a
        c = (a**2 + b**2)**0.5
        d = a/2

        t.fillcolor('green')
        t.begin_fill()
        t.right(45)
        t.forward(c)
        t.right(135)
        t.forward(b+b)
        t.right(135)
        t.forward(c)
        t.end_fill()
        t.right(135)
        t.forward(d)
        t.left(90)
        a*=1.5

    t.fillcolor('brown')
    t.right(90)
    t.forward(d)
    t.left(90)
    t.begin_fill()
    t.forward(b/3)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(b/1.5)
    t.right(90)
    t.forward(50)
    t.end_fill()

t.up()
t.goto(0,200)
DrawChristmasTree(45)

turtle.Screen().exitonclick()
