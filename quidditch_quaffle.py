from turtle import Turtle


class Quaffle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("maroon")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.075

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_keeper(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_keeper()
        self.move_speed = 0.075
