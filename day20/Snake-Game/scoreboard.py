from turtle import Turtle

ALIGNEMENT = "center"
FONT = ('arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_score()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updatescoreboard()


    def updatescoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} high score: {self.high_score}", move=False, align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_score()
        self.score = 0
        self.updatescoreboard()

    def update_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def get_score(self):
        with open("data.txt") as file:
            return int(file.read())

    def scoreboardincrease(self):
        self.score += 1
        self.updatescoreboard()
