# Hirst Painting Project
# Grid size can be changed by modifying no_of_dots (must be a perfect square).
# Space between dots is 50 pixels.
import turtle as t
import random

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.speed(0)
t.colormode(255)
# no_of_dots going to be a perfect square
no_of_dots = 100

dots_in_row = int(no_of_dots**(1/2))

def start_pt(dots_in_row):
    x = (dots_in_row-1)*25
    tim.up()
    tim.backward(x)
    tim.right(90)
    tim.forward(x)
    tim.left(90)
    tim.down()


def row_print(dots_in_row):
    
    for _ in range(dots_in_row):
        tim.dot(20, random.choice(color_list))
        tim.up()
        if _ != dots_in_row - 1:
            tim.forward(50)
        tim.down()


def next_col(dots_in_row):
    y = (dots_in_row-1)*50
    tim.up()
    tim.backward(y)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.down()


start_pt(dots_in_row)
for row in range(dots_in_row):
    row_print(dots_in_row)
    if row != dots_in_row -1:
        next_col(dots_in_row)

screen = t.Screen()
screen.exitonclick()