
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
s = 0
for _ in range(0,3):
    snake = Turtle('square')
    snake.color('white')
    snake.penup()
    snake.goto(x=10+s,y=10)
    s+=20






screen.exitonclick()