##import turtle
##
##wn = turtle.Screen()
##
##mosta = turtle.Turtle()
##
##mosta.shape("turtle") #the shape
##
##mosta.speed(2) # 1 is the slowest, 10 is the fastest
##
##for i in range(4):
##    mosta.forward(150)
##    mosta.left(90)
##
##wn.exitonclick()

#Draw with turtle
#----------------

##import turtle
##
##wn = turtle.Screen()
##wn.bgcolor("lightgreen")
##
##mosta = turtle.Turtle()
##mosta.color("blue")
##mosta.shape("turtle")
##
##mosta.up() #pick the pen up
##
##for size in range(5, 100, 2):
##    mosta.stamp() #stamp the turtle in the canvas
##    mosta.forward(size)
##    mosta.right(30)
##
##wn.exitonclick()

import turtle

wn = turtle.Screen()
jose = turtle.Turtle()

jose.shape("turtle")

jose.penup()

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)



wn.exitonclick()
