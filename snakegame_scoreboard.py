from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.score = 0
        self.levels = level
        if self.levels == 1:
            with open("snake_highscores/snakegame_highscore_easy.txt") as data:
                self.high_score = int(data.read())
        elif self.levels == 2:
            with open("snake_highscores/snakegame_highscore_medium.txt") as data:
                self.high_score = int(data.read())
        elif self.levels == 3:
            with open("snake_highscores/snakegame_highscore_hard.txt") as data:
                self.high_score = int(data.read())
        self.color("#49b386")
        self.penup()
        self.hideturtle()
        self.goto(0, 212)
        self.write("Chamber of Secrets", align="center", font=("Harry P", 30, "normal"))
        self.goto(250, 220)
        self.write(f"High Score: {self.high_score}", align="center", font=("Harry P", 25, "normal"))
        self.goto(400, 220)
        self.write(f"Score: {self.score}", align="center", font=("Harry P", 25, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.clear()
            self.goto(0, 212)
            self.write("Chamber of Secrets", align="center", font=("Harry P", 30, "normal"))
            self.goto(250, 220)
            self.write(f"High Score: {self.score}", align="center", font=("Harry P", 25, "normal"))
            self.goto(400, 220)
            self.write(f"Score: {self.score}", align="center", font=("Harry P", 25, "normal"))
        else:
            self.clear()
            self.goto(0, 212)
            self.write("Chamber of Secrets", align="center", font=("Harry P", 30, "normal"))
            self.goto(250, 220)
            self.write(f"High Score: {self.high_score}", align="center", font=("Harry P", 25, "normal"))
            self.goto(400, 220)
            self.write(f"Score: {self.score}", align="center", font=("Harry P", 25, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            if self.levels == 1:
                with open("snake_highscores/snakegame_highscore_easy.txt", mode="w") as data:
                    data.write(f"{self.score}")
            elif self.levels == 2:
                with open("snake_highscores/snakegame_highscore_medium.txt", mode="w") as data:
                    data.write(f"{self.score}")
            elif self.levels == 3:
                with open("snake_highscores/snakegame_highscore_hard.txt", mode="w") as data:
                    data.write(f"{self.score}")
            self.clear()
            self.goto(0, 212)
            self.write("Chamber of Secrets", align="center", font=("Harry P", 30, "normal"))
            self.goto(250, 220)
            self.write(f"High Score: {self.score}", align="center", font=("Harry P", 25, "normal"))
            self.goto(400, 220)
            self.write(f"Score: {self.score}", align="center", font=("Harry P", 25, "normal"))
        self.color("black")
        self.goto(0, 10)
        self.write("Game over!\n", align="center", font=("Harry P", 32, "bold"))
        self.goto(0, -20)
        self.write(f"Your final score is {self.score}.", align="center", font=("Harry P", 32, "bold"))
