import time
import turtle
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()
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
def to_exit():
    global game_on
    game_on=False
screen.onkeypress(to_exit,"f")
ball_speed = 0.1
while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    if ball.ball.distance(r_paddle.paddle)< 50 and ball.ball.xcor() >330:
        ball.change_directions_for_right()
        ball_speed*=0.8
    elif ball.ball.distance(l_paddle.paddle) < 50 and ball.ball.xcor() <-330:
        ball.change_directions_for_left()
        ball_speed *= 0.8
    if ball.ball.xcor() >380 or ball.ball.xcor() < -380:
        ball.reset()
        if ball.ball.xcor() < -380:
            scoreboard.r_score+=1
        else:
            scoreboard.l_score+=1
        ball = Ball()
        ball_speed = 0.1

        scoreboard.update_score()
screen.exitonclick()
