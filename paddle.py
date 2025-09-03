from turtle import Turtle
class Paddle:
    def __init__(self,left_right):
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.shapesize(5, 1)
        self.paddle.color("white")
        self.paddle.goto(left_right, 0)

    def go_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def go_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)