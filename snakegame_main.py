from turtle import Screen
import time
from snakegame_snake import Snake
from snakegame_food import Food
from snakegame_scoreboard import Scoreboard
from tkinter import messagebox


def snake_game():
    level = int(input("Which level do u want to play?\nChoose 1 for easy\nChoose 2 for medium\nChoose 3 for hard\n"))
    level_on = True
    while level_on:
        if level == 1:
            time_del = 0.1
            scoreboard = Scoreboard(level)
            level_on = False
        elif level == 2:
            time_del = 0.075
            scoreboard = Scoreboard(level)
            level_on = False
        elif level == 3:
            time_del = 0.05
            scoreboard = Scoreboard(level)
            level_on = False
        else:
            print("Please enter a valid input.")
    screen = Screen()
    screen.setup(width=996, height=560)
    screen.bgpic("chamber_of.gif")
    screen.title("Play snake")
    screen.tracer(0)
    food = Food()
    snake = Snake()
    screen.listen()
    screen.onkey(snake.mup, "Up")
    screen.onkey(snake.mdown, "Down")
    screen.onkey(snake.mleft, "Left")
    screen.onkey(snake.mright, "Right")
    screen.onkey(snake.mup, "w")
    screen.onkey(snake.mdown, "s")
    screen.onkey(snake.mleft, "a")
    screen.onkey(snake.mright, "d")
    game_on = True
    messagebox.showinfo("Directions", "Press W, A, S, D or the arrow keys to navigate and after the completion "
                                      "of the game, click on the screen to exit.")
    time.sleep(1)
    while game_on:
        screen.update()
        time.sleep(time_del)
        snake.move()
        if snake.turtles[0].distance(food) < 15:
            snake.snake_incr()
            food.refresh()
            scoreboard.increase_score()
        if (snake.turtles[0].xcor() > 496 or snake.turtles[0].xcor() < -496 or
                snake.turtles[0].ycor() < -280 or snake.turtles[0].ycor() > 280):
            scoreboard.game_over()
            game_on = False
        for tim in snake.turtles[1:]:
            if snake.turtles[0].distance(tim) < 10:
                scoreboard.game_over()
                game_on = False
    screen.exitonclick()
