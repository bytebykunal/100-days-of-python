import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    
    #car generation and movement
    cars.car_generator()
    cars.move_car()

    #reaching finishline 
    if player.ycor() >= player.finish_line:
        scoreboard.next_level()
        player.refresh()
        cars.speed_up()

    #Collision with car
    for car in cars.all_cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False
            break


screen.exitonclick()