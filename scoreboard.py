from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.update_scoreboard()
        self.increase_level()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
