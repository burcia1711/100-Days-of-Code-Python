
import random
from turtle import Turtle, Screen

screen = Screen ()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red","orange", "gold", "green","blue", "purple"]
y_position=-70
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position+=30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
new_screen = Screen()
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            screen.clear()

            if winning_color == user_bet:
                turtle.setposition(-120, 0)
                turtle.write(f"You've won! The {winning_color} turtle is the winner!", move=False, align="left", font=['Calibri', 12, "bold"])
            else:
                turtle.setposition(-120, 0)
                turtle.write(f"You've lost! The {winning_color} turtle is the winner!", align="left", font=['Calibri', 12, "bold"])
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()