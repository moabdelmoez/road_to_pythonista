import random
import turtle

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = - w.window_height() / 2

    turtleX = t.xcor()
##    print(turtleX)
    turtleY= t.ycor()
##    print(turtleY)

    stillIn = True

    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

wn = turtle.Screen()
t = turtle.Turtle()

t.shape('turtle')

while isInScreen(wn, t):
    coin = random.randrange(0,2)
##    print(coin)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()
