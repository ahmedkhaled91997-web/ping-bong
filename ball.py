from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.x_move = random.randint(-10,-1)
        self.y_move = random.randint(3,10)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
    def reset_position(self):
        self.goto(0, 0)
            
      
    

        