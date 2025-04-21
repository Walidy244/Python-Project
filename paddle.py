from turtle import Turtle





class Paddle(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.setpos(width, height)  # or self.goto(350,0)
#NOW SELF IS REFERRING TO THE OBJECT THAT WE CREATED FOR THIS CLASS
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)











