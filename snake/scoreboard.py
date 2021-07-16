from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align='center', font=('Arial',20,'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))

    def defeat(self):
        self.clear()
        self.write(f"Game over!", align='center', font=('Arial', 20, 'normal'))
