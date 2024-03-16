from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
DIST = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("#49b386")
        new_segment.penup()
        new_segment.goto(position)
        self.turtles.append(new_segment)

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
        self.turtles[0].forward(DIST)

    def snake_incr(self):
        self.add_segment(self.turtles[-1].position())

    def mup(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def mdown(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def mleft(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def mright(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
