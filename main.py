from turtle import Turtle, Screen
import random

t = Turtle()
color = ["blue", "yellow", "purple", "green", "black", "red", "pink"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for i in range(3, 11):
    draw_shape(i)
    t.color(random.choice(color))

screen = Screen()
screen.exitonclick()
