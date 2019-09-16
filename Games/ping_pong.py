import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# wn.tracer(0)

# score variables
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 #delta, ball move by 2 pixels
ball.dy = -2 #delta, ball move by 2 pixels

# pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=("Courier", 24, "normal"))

# Move paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 # add 20 pixels to y
    paddle_a.sety(y)

# Move paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 # subtract 20 pixels to y
    paddle_a.sety(y)


# Move paddle b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 # add 20 pixels to y
    paddle_b.sety(y)

# Move paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 # subtract 20 pixels to y
    paddle_b.sety(y)


# keyboard binding
wn.listen()

# when a user press w, the paddle moves up
wn.onkeypress(paddle_a_up, 'w')

# when a user press s, the paddle moves down
wn.onkeypress(paddle_a_down, 's')

# when a user press up arrow, the paddle moves up
wn.onkeypress(paddle_b_up, 'Up')

# when a user press down arrow, the paddle moves down
wn.onkeypress(paddle_b_down, 'Down')
   

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # up-bottom border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse a direction
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT|winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverse a direction
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT|winsound.SND_ASYNC)

    # right-left border check
    if ball.xcor() > 390:
        ball.goto(0, 0) # go back to the middle of the screen
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0) # go back to the middle of the screen
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 24, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT|winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT|winsound.SND_ASYNC)
