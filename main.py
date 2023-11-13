
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

positions = [(0,0), (-20, 0), (-40, 0)]

for pos in positions:
    snake = Turtle('square')
    snake.color('white')
    snake.penup()
    snake.goto(pos)






screen.exitonclick()