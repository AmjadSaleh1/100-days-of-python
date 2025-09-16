import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make ur bet", prompt="which title will win the race ? write a color")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! the color of the turtle that won is {winning_color}")
            else:
                print(f"you lost! the color of the turtle that won is {winning_color}")
        distince = random.randint(0, 10)
        turtle.forward(distince)
screen.exitonclick()
