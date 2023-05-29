import turtle
turtle.title("Turtle Example")


t = turtle.Turtle()
t.shape("turtle")

# Draw the alphabet S
# t.up()
# t.left(90)
# t.forward(180)
# t.down()
# t.right(90)
# size = -120 # Change to whatever size you want, but as a negative number
# degrees = -180 # Change degrees to match half a circle, HINT 360/2
# t.circle(size,degrees)
# size = 120 # Change to whatever size you want, but as a negative number
# degrees = -180 # Change degrees to match half a circle, HINT 360/2
# t.circle(size,degrees)
# Draw the alphabet G
size = -120 # Change to whatever size you want, but as a negative number
degrees = -180 # Change degrees to match half a circle, HINT 360/2
t.circle(size,degrees)
t.right(90)
t.forward(90)
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)
turtle.Screen().exitonclick()