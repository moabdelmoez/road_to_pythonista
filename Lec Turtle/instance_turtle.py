#Instances - A herd of turtles
#-----------------------------

import turtle

wn = turtle.Screen() #set up the window and its attributes
wn.bgcolor("green")

tess = turtle.Turtle() #create tess and some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle() #create alex


tess.forward(80) #Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120) #complete the triangle

tess.right(180) #turn tess around
tess.forward(80) #move her away from the origin

alex.forward(50) #make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()

###Draw a Circle
###-------------
##
##import turtle
##
##wn = turtle.Screen()
##mosta = turtle.Turtle()
##
##mosta.circle(60)
