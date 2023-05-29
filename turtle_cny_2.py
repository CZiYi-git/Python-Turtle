import turtle
import math
turtle.title("Turtle CNY")


t = turtle.Turtle()
t.speed(10)

# Put your draw Ang Bao function below
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
    t.goto(50,25)
    writeWord()
    
# Put your draw Orange function below
def drawOrange():
    x=50
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(x,360)
    t.end_fill()
    






font = ('arial',50,'bold')
t.up()

t.color('red')
t.goto(0,200)
t.write('新年快乐',align='center', font=font)
t.goto(0,100)
t.write('年年有余',align='center', font=font)

t.up()
t.goto(0,-50)
t.left(90)
drawAngBao()
t.goto(-30,-50)
t.right(90)
drawOrange()


turtle.Screen().exitonclick()