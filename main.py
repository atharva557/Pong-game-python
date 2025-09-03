import time
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


game_on = True
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()