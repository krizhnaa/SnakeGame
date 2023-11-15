from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.write(f'Scoreboard : {self.score}', align='center', font=('Arial', 15, 'normal'))
        # self.write((0, 220), False)