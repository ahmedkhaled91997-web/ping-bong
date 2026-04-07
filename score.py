from turtle import Turtle
class Score(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    def calculation_score(self,):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}",align="center",font=("Courier", 40, "normal"))
    def l_point(self):
        self.l_score += 1
        self.calculation_score()
    def r_point(self):
        self.r_score += 1
        self.calculation_score()

        