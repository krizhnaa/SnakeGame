
from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def sh():
    return snake.head


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if sh().distance(food) < 15:
        scoreboard.scored()
        snake.addtail()
        food.refresh()
        screen.update()

    if sh().xcor() > 280 or sh().xcor() < -280 or sh().ycor() > 280 or sh().ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()
