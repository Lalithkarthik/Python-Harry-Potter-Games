from turtle import Screen
from quidditch_keeper import Keeper
from quidditch_scoreboard import Scoreboard
from quidditch_quaffle import Quaffle
import time
from tkinter import messagebox
import ctypes


def quidditch():
    print("Which houses do you want to play for?\nChoose 1 for Gryffindor, 2 for Hufflepuff, 3 for Slytherin, 4 for Ravenclaw: ")
    l_col_on = True
    r_col_on = True
    while l_col_on:
        left = int(input("Team playing on the left is: "))
        if left == 1:
            coll = "red"
            l_col_on = False
        elif left==2:
            coll = "yellow"
            l_col_on = False
        elif left==3:
            coll = "green"
            l_col_on = False
        elif left == 4:
            coll = "blue"
            l_col_on = False
        else:
            print("Please enter a valid input.")
        while r_col_on:
            right = int(input("Team playing on the right is: "))
            if right == 1:
                colr = "red"
                r_col_on = False
            elif right == 2:
                colr = "yellow"
                r_col_on = False
            elif right == 3:
                colr = "green"
                r_col_on = False
            elif right == 4:
                colr = "blue"
                r_col_on = False
            else:
                print("Please enter a valid input.")
    screen = Screen()
    screen.title("Quidditch Keepers - Save the goals!")
    screen.setup(800, 500)
    screen.bgpic("quidditch.gif")
    screen.tracer(0)
    sly_keeper = Keeper((-380, 0), coll)
    gry_keeper = Keeper((373, 0), colr)
    quaffle = Quaffle()
    scores = Scoreboard(left, right)
    screen.listen()
    screen.onkey(gry_keeper.move_up, "Up")
    screen.onkey(sly_keeper.move_up, "w")
    screen.onkey(gry_keeper.move_down, "Down")
    screen.onkey(sly_keeper.move_down, "s")
    game_on = True
    messagebox.showinfo("Directions", "Use W, A to control the left keeper and the Up, Down to control the right keeper, and after the completion of the game, click on the screen to exit.")
    time.sleep(2)
    while game_on:
        time.sleep(quaffle.move_speed)
        screen.update()
        quaffle.move()
        if quaffle.ycor() > 230 or quaffle.ycor() < -229:
            quaffle.bounce_wall()
        if quaffle.distance(gry_keeper) < 50 and quaffle.xcor() > 345 or quaffle.distance(sly_keeper) < 50 and quaffle.xcor() < -350:
            quaffle.bounce_keeper()
        if quaffle.xcor() > 380:
            quaffle.reset_pos()
            scores.l_inc()
        if quaffle.xcor() < -388:
            quaffle.reset_pos()
            scores.r_inc()
        if scores.l_score == 5 or scores.r_score == 5:
            screen.exitonclick()

