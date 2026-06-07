from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()
    
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()