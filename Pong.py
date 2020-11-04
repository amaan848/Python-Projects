
import turtle
import os
wn = turtle.Screen()
wn.title("Pong by @Amaaniqbal")
wn.bgcolor("black")
wn.setup(height = 600, width = 800)
wn.tracer(0)

#Score
score_a = 0
score_b = 0
#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1,stretch_wid=5) #the number 5 and 1 are the times the paddle is going to strech, its default is 20 * 20 pixels
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1,stretch_wid=5) #the number 5 and 1 are the times the paddle is going to strech, its default is 20 * 20 pixels
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2.5
ball.dy = 2.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A: 0  PLAYER B: 0 ", align="center",font=("Courier", 24, "normal"))


#function part

def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up , "w")
wn.onkeypress(paddle_a_down , "s")
wn.onkeypress(paddle_b_up , "Up")
wn.onkeypress(paddle_b_down , "Down")

#main game loop
while score_a<5 and score_b<5:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1
        os.system("afplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        os.system("afplay bounce.wav&")
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"PLAYER A: {score_a}  PLAYER B: {score_b} ", align="center",font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"PLAYER A: {score_a}  PLAYER B: {score_b} ", align="center",font=("Courier", 24, "normal"))
    #paddle and ball collisions
    if (340 < ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1
    




