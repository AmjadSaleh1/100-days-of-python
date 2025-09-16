from turtle import Turtle, Screen
import turtle as t
import random


tim = Turtle()
t.colormode(255)
direction = [0, 90, 180, 270]
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.color(random_color())
        tim.circle(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


draw_spirograph(5)

# def random_walk():
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(30)


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)


# for i in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

# for i in range(100):
#     random_walk()

screen = Screen()
screen.exitonclick()
