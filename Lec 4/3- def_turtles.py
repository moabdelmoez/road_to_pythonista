##import turtle
##
##def drawSquare(t, sz):
##    """Make turtle t draw a square of with side sz."""
##    for i in range(4):
##        t.forward(sz)
##        t.left(90)
##
##wn = turtle.Screen()
##wn.bgcolor("lightgreen")
##
##mosta = turtle.Turtle()
##drawSquare(mosta, 100)
##
##wn.exitonclick()

###############################################################

##import turtle
##
##def drawSquare(t, sz):
##    """Make turtle t draw a square of with side sz."""
##
##    for i in range(4):
##        t.forward(sz)
##        t.left(90)
##
##
##wn = turtle.Screen()          # Set up the window and its attributes
##wn.bgcolor("lightgreen")
##
##alex = turtle.Turtle()        # create alex
##alex.speed(2)
##alex.shape("turtle")
##drawSquare(alex, 50)          # Call the function to draw the square
##
##alex.penup()
##alex.goto(100,100) # go to long/lat 100 and 100 or cordinates x,y
##alex.pendown()
##
##drawSquare(alex,75)           # Draw another square
##
##wn.exitonclick()

#################################################################

import turtle

def drawMulticolorSquare(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(20):
    drawMulticolorSquare(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()

