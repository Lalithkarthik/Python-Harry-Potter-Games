from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, coll, colr):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.hleft = ""
        self.hright = ""
        self.update_scores()
        if coll == 1:
            self.hleft = "Gryffindor"
        elif coll == 2:
            self.hleft = "Hufflepuff"
        elif coll == 3:
            self.hleft = "Slytherin"
        elif coll == 4:
            self.hleft = "Ravenclaw"
        if colr == 1:
            self.hright = "Gryffindor"
        elif colr == 2:
            self.hright = "Hufflepuff"
        elif colr == 3:
            self.hright = "Slytherin"
        elif colr == 4:
            self.hright = "Ravenclaw"

    def update_scores(self):
        self.goto(-100, 170)
        self.write(self.l_score, align="center", font=("Harry P", 40, "normal"))
        self.goto(100, 170)
        self.write(self.r_score, align="center", font=("Harry P", 40, "normal"))

    def l_inc(self):
        self.l_score += 1
        self.clear()
        self.update_scores()
        self.check_end_game()

    def r_inc(self):
        self.r_score += 1
        self.clear()
        self.update_scores()
        self.check_end_game()

    def check_end_game(self):
        if self.r_score == 5:
            self.goto(0, 0)
            self.write(f"{self.hright} beats {self.hleft}! The final score is {self.l_score} - {self.r_score}.", align="center", font=("Harry P", 30, "normal"))
        elif self.l_score == 5:
            self.goto(0, 0)
            self.write(f"{self.hleft} beats {self.hright}! The final score is {self.l_score} - {self.r_score}.", align="center", font=("Harry P", 30, "normal"))
