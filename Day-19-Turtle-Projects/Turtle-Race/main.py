from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height= 400)


user_bet = screen.textinput("Make your bet.", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-75, -45, -15, 15, 45, 75]

all_turtles = []


#draws finish line
management_turtle = Turtle()
management_turtle.hideturtle()
management_turtle.penup()
management_turtle.goto(230, -100)
management_turtle.pendown()
management_turtle.width(7)
management_turtle.goto(230, 100)






for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    user_bet = user_bet.lower()
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor()>=230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
            
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

screen.exitonclick()
