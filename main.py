import turtle

import colorgram
from turtle import Turtle, Screen
import random
turtle.colormode(255)
# TODO-1: Color extraction from the damien image:
# colors = colorgram.extract('damien.jpg', 30)
# color_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color_list.append((r, g, b))


colors_extracted = [(233, 239, 246), (246, 239, 242), (132, 166, 205), (221, 148, 106),
                    (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
                    (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
                    (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
                    (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

jack = Turtle()
jack.penup()
jack.hideturtle()
jack.speed(10)
jack.setheading(225)
jack.forward(250)
jack.setheading(0)
for i in range(1, 101):
    jack.dot(20, random.choice(colors_extracted))
    jack.forward(50)
    if i % 10 == 0:
        jack.setheading(90)
        jack.forward(50)
        jack.setheading(180)
        jack.forward(500)
        jack.setheading(0)
screen = Screen()
screen.exitonclick()
