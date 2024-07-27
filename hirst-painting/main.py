import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg',10)
color_list = []

for dot in colors:
    color = (dot.rgb.r, dot.rgb.g, dot.rgb.b)
    color_list.append(color)

t = Turtle()
screen = Screen()
print(screen.colormode(255))
direction = True

for x in range(10):
    for y in range(10):
        circle_color = color_list[random.randint(0,len(color_list)-1)]
        t.fillcolor(circle_color)
        t.pencolor(circle_color)
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        if y < 9:
            t.forward(30)
    if direction:
        t.left(90)
        t.forward(50)
        t.left(90)
        direction = False
    else:
        t.right(90)
        t.forward(10)
        t.right(90)
        direction = True
    t.pendown()



screen.exitonclick()
