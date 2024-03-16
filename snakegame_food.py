from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("gold", "#ed3e44")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-353, 353)
        y = random.randint(-203, 203)
        self.goto(x, y)
