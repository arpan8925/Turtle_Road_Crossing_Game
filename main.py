import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    #Detection collision with cars
    for cars in car.allcars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finishing_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()



screen.exitonclick()
