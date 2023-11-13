from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions = [(0,0), (-20, 0), (-40, 0)]
        self.segments = []

    def move(self):
        for pos in self.positions:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)
        self.segments[0].forward(20)
        self.segments[0].left(90)
