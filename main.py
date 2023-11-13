
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

positions = [(0,0), (-20, 0), (-40, 0)]
segments = []
is_game_on = True

for pos in positions:
    snake = Turtle('square')
    snake.color('white')
    snake.penup()
    snake.goto(pos)
    segments.append(snake)



while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)





screen.exitonclick()