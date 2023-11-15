from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Scoreboard : {self.score}', align='center', font=('Arial', 15, 'normal'))

    def scored(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

