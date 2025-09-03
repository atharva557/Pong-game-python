import time
import turtle
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
turtle.pencolor("white")
turtle.hideturtle()
turtle.penup()
turtle.setheading(270)
turtle.backward(300)

for i in range(15):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

game_on = True
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
while game_on:
    time.sleep(0.091)
    screen.update()
    ball.move()
    if ball.ball.distance(r_paddle.paddle)< 50 and ball.ball.xcor() >330:
        ball.change_directions_for_right()
    elif ball.ball.distance(l_paddle.paddle) < 50 and ball.ball.xcor() <-330:
        ball.change_directions_for_left()
    if ball.ball.xcor() >380 or ball.ball.xcor() < -380:
        ball = Ball()

screen.exitonclick()