from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score is {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align="left", font=FONT)
    