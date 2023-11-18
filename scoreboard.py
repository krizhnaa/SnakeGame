from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}      High Score : {self.highscore}', align='center', font=('Arial', 15, 'normal'))

    def scored(self):
        self.score += 1
        self.update_scoreboard()

    def resrt(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

