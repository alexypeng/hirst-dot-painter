# Hirst Dot Painting program created by Alexander Peng on 2024/08/04. Focuses on the turtle package and
# creating graphics in Python.

import colorgram
from turtle import Turtle, Screen
import random

colours = colorgram.extract("image.jpg", 91) # Extracts all the colours from the image
rgb_colours = []

# Adding all the colours in RGB format to a list of tuples
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    if r < 235 or b < 235 or g < 235:
        rgb_colours.append((r, g, b))


def paint(x, y):
    """Paints the Hirst Dot Painting. Inputs take number of dots in the x and number of dots in the y"""
    width = 500 / x
    height = 500 / y
    if x > y:
        dot_size = 500 / 3 / x
    else:
        dot_size = 500 / 3 / y
    for i in range(y):
        t.goto(0 - width * (x - 1) / 2, 0 - height * (y - 1) / 2 + i * height) # Sets the position of the Turtle to be
        # half a step away from the edge. y position increments
        for j in range(x):
            t.dot(dot_size, rgb_colours[random.randint(0, len(rgb_colours) - 1)])
            t.forward(width)


t = Turtle()
t.speed("fastest")
t.up()


screen = Screen()
screen.setup(width=500, height=500)
screen.colormode(255)

paint(5, 5)
t.hideturtle()

screen.exitonclick()
