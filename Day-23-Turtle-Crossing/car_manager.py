from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.start = 320
        self.x_move= STARTING_MOVE_DISTANCE
        self.all_cars = []
        
    def car_generator(self):
            random_chance = random.randint(1, 6)
            if random_chance == 1:
                car = Turtle("square")
                car.penup()
                car.color(random.choice(COLORS))
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.goto(300, random.randint(-250, 250))
                self.all_cars.append(car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.x_move)
    def speed_up(self):
        self.x_move += MOVE_INCREMENT

    
