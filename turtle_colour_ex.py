import turtle
turtle.title("Turtle fill exercise")

t = turtle.Turtle()
t.shape("turtle")

# Draw a square and fill it up with the colour 'red'
# t.fillcolor('red')
# t.begin_fill()
# t.forward(90)
# t.right(90)
# t.forward(90)
# t.right(90)
# t.forward(90)
# t.right(90)
# t.forward(90)
# t.right(90)
# t.end_fill()
# Draw a semi circle and fill it up with the colour 'green'
# t.fillcolor('green')
# t.begin_fill()
# size = 50 # Change to whatever size you want, but as a negative number
# degrees = -180 # Change degrees to match half a circle, HINT 360/2
# t.circle(size,degrees)
# t.left(90)
# t.forward(100)
# t.end_fill()

# Draw a star and fill it up with the colour 'blue'
t.speed(0)
t.up()
t.fillcolor('blue')
t.begin_fill()
# t.left(90)

# t.left(210)



for i in range(5):
    t.right(180-36)
    t.forward(90)

t.end_fill()
 
turtle.Screen().exitonclick()
