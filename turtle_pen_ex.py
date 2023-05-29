import turtle
turtle.title("Turtle fill exercise")

t = turtle.Turtle()
t.shape("turtle")

# Draw 2 square eyes with a gap between them

# Draw 2 semi circle eyes with a gap between them
# t.left(90)
# size = -50 # Change to whatever size you want, but as a negative number
# degrees = 180 # Change degrees to match half a circle, HINT 360/2
# t.circle(size,degrees)
# t.up()
# t.right(90)
# t.forward(120)
# t.right(90)
# t.down()
# size = 50 # Change to whatever size you want, but as a negative number
# degrees = 180 # Change degrees to match half a circle, HINT 360/2
# t.circle(size,degrees)
# Draw a face with square or semi circle as eyes
t.up()
t.right(180)
t.forward(100)
t.down()
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(180)
t.up()
t.forward(360)
t.left(90)
t.forward(20)
t.down()
size = 50 # Change to whatever size you want, but as a negative number
degrees = 180 # Change degrees to match half a circle, HINT 360/2
t.circle(size,degrees)
t.up()
t.forward(100)
t.right(90)
t.forward(30)
t.right(90)
t.down()
size = 50 # Change to whatever size you want, but as a negative number
degrees = -180 # Change degrees to match half a circle, HINT 360/2
t.circle(size,degrees)

turtle.Screen().exitonclick()



