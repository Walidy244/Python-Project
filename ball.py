from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")#historrically the ball was square
        self.color("white")
        self.move_x=10
        self.move_y=10
        self.penup()
        self.move_speed=0.1
    def move(self):
        new_x = self.xcor() +self.move_x
        new_y = self.ycor() +self.move_y
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.move_y *= -1
    def bounce_x(self):
        self.move_x *= -1
    def defaultpos(self):
        self.goto(0, 0)