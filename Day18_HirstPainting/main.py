# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("download.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(211, 210, 209), (189, 167, 125), (210, 213, 217), (60, 91, 111), (155, 89, 67), (113, 43, 36), (55, 40, 38), (170, 183, 168), (132, 161, 171), (137, 149, 70), (102, 78, 86), (85, 128, 106), (109, 39, 46), (38, 59, 46), (176, 151, 153), (207, 197, 139), (74, 40, 43), (178, 103, 83), (34, 62, 76), (36, 71, 87), (108, 142, 109), (210, 183, 177), (50, 71, 58), (148, 117, 121), (41, 67, 87), (180, 196, 201)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()