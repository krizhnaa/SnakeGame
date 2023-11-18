from turtle import Turtle


mov_dist = 20
up = 90
down = 270
right = 0
left = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in self.positions:
            self.addseg(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg_num - 1].xcor()
            y_new = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_new, y_new)

        self.head.forward(mov_dist)

    def addseg(self, pos):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def restrt(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def addtail(self):
        self.addseg(self.segments[-1].position())

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
