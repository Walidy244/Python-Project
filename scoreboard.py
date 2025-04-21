from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()#this will clear both of the scores and update them at the same time
        self.goto(-100, 200)
        # turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def leftside_point(self):
        self.r_score += 1
        self.update_scoreboard()#WE NEED TO UPDATE THE SCOREBOARD EACH TIME WE SCORE A POINT
    def rightside_point(self):
        self.r_score += 1
        self.update_scoreboard()#WE NEED TO UPDATE THE SCOREBOARD EACH TIME WE SCORE A POINT