###turtle and for statement
###------------------------
##
##import turtle
##
##wn = turtle.Screen()
##
##mosta = turtle.Turtle()
##
###for i in [0,1,2,3]:
##for i in range(0,4):
##    mosta.forward(50)
##    mosta.left(90)
##
##wn.exitonclick()

#turtle and for statement
#------------------------

import turtle

wn = turtle.Screen()

mosta = turtle.Turtle()

for color in ["yellow", "red", "blue", "green"]:
    mosta.color(color)
    mosta.forward(200)
    mosta.left(90)

wn.exitonclick()
