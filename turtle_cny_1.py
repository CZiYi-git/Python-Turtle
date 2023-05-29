import turtle
import math
turtle.title("Turtle Angbao")


t = turtle.Turtle()

t.speed(10)

# Write a function to draw an angbao!
def drawAngBao():

    # Use this function to write 福!
    def writeWord():
        font = ('arial',x,'bold')
        t.color('Yellow')
        t.write('福',align='center', font=font)

    # You may change the size ratio
    x=50
    width = x*2
    height = x*3

    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)

    t.end_fill()
    t.goto(50,-75)
    writeWord()
# Write a function to draw an orange!
def drawOrange():
    # You may change the size ratio
    x=50
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(x,360)
    t.end_fill()

t.up()
t.right(90)
t.goto(100,0)
drawAngBao()
t.goto(-100,-100)
drawOrange()


turtle.Screen().exitonclick()