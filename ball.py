import random
from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball=Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.setheading(random.randrange(0, 360, 40))
    def move(self,):
        if self.ball.ycor() > 280:
            self.ball.setheading(-self.ball.heading())
        if self.ball.ycor() <-280:
            self.ball.setheading(-self.ball.heading())
        self.ball.forward(10)
    def bounce(self):
        new_head = 360-self.ball.heading()
        self.ball.setheading(new_head)
    def change_directions_for_left(self):
        new_heading = 180 - self.ball.heading()
        self.ball.setheading(new_heading)
    def change_directions_for_right(self):
        new_heading = 180 - self.ball.heading()
        self.ball.setheading(new_heading)
    def reset(self):
        self.ball.hideturtle()
