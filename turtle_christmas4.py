import turtle
import math
turtle.title("Turtle Example")


t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
# Put your draw house function
def DrawHouse(a):

    b = a * 4
    c = (a**2 + b**2)**0.5
    d = a/2
    
    angle_b = math.tan(a/b) * (180/math.pi)
    angle_a = 180 - angle_b - angle_b 

    house_height = 0.5 * 2 * b
    house_width = 0.6 * 2 * b
    door_width = house_width/3
    door_height = house_height/1.5
    r = d
    
    t.up()
    t.fillcolor('cyan')
    t.begin_fill()
    t.right(90-angle_a/2)
    t.forward(c)
    t.right(180-angle_b)
    t.forward(b+b)
    t.right(180-angle_b)
    t.forward(c)
    t.end_fill()
    t.right(180-angle_a/2)
    t.forward(a*1.05)
    t.right(90)
    t.fillcolor('brown')
    t.begin_fill()
    t.forward(house_width/2)
    t.left(90)
    t.forward(house_height)
    t.left(90)
    t.forward(house_width)
    t.left(90)
    t.forward(house_height)
    t.left(90)
    t.forward(house_width/2)
    t.end_fill()
    t.right(180)
    t.forward(house_width/2)
    t.right(90)
    t.forward(house_height)
    t.right(90)
    t.forward(0.1*house_width)
    t.right(90)
    t.fillcolor('cyan')
    t.begin_fill()
    t.forward(door_height)
    t.left(90)
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.left(90)
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.circle(door_width/2,180)
    t.end_fill()
    t.right(90)
    t.forward(60)
    t.left(180)
    t.forward(10)
    t.up()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(r,360)
    t.end_fill()
    t.left(90)
    t.down()
    t.forward(a)
    t.up()
    t.circle(r,-360/4)
    t.down()
    t.forward(a)
    t.up()
    t.forward(70-a)
# Put your draw tree function
def DrawChristmasTree(a):
    
    trunk_width = 45
    trunk_height = trunk_width*1.5
    t.up()
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

# font = ('arial',50,'bold')
# t.up()

# t.color('red')
# t.goto(0,300)
# t.write('Write text here',align='center', font=font)
# t.goto(0,200)
# t.write('Write christmas greeting here',align='center', font=font)



# Use draw christmas tree function here
DrawChristmasTree(45)
# use draw house function here
t.right(55)
t.forward(300)
t.right(35)
DrawHouse(45)

turtle.Screen().exitonclick()