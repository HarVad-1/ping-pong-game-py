import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

TIME=0.1

screen = Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800, height=600)
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

score=Scorecard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    # detection of the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detection of the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detection if the ball has missed
    if ball.xcor()>380:
        ball.reset()
        score.left_()

    if ball.xcor()<-380:
        ball.reset()
        score.right_()

screen.exitonclick()
