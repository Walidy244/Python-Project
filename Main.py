from turtle import Screen, Turtle
from paddle import Paddle# we are importing the class Paddle from my file paddle
from ball import Ball
import time
from scoreboard import Scoreboard
#SETIING UP THE SCREEN
screen =Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong The Arcade Game")
screen.tracer(10)# then tracer method controls the animation and in order to turn off the animation we can put a zero in the method

#OBJECTS
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()

#USING SCREENLISTEN TO USE AND LISTEN TO KEYBINDS
screen.listen()# for the screen to listen to key strokes (keybinds)
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

#UPDATES THE SCREEN EVERYTIME WE CLICK SOMETHING

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()# constantly refresh the screen
    ball.move()
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
        #detecting if the ball goes out of bounds
    elif ball.xcor()>410:
        ball.defaultpos()
        ball.bounce_x()
        scoreboard.rightside_point()
    elif ball.xcor()<-410:
        ball.defaultpos()
        ball.bounce_x()
        scoreboard.leftside_point()
        # detecting collision with the right paddle and left paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        ball.move_speed = max(0.04, ball.move_speed - 0.01)
screen.exitonclick()













