from turtle import Screen
from racquer import PingRacquet
from ball import Ball 
from score import Score
import time
window = Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

R_player = PingRacquet((350, 0))
L_player = PingRacquet((-350, 0))
ball = Ball()
score=Score("red",(0,240))


window.listen()
window.onkeypress(R_player.move_up, "Up")
window.onkeypress(R_player.move_down, "Down")
window.onkeypress(L_player.move_up, "w")
window.onkeypress(L_player.move_down, "s")
speed=(0.04)

game_is_on = True 
while game_is_on:
    score.calculation_score()
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:# ارتداد الكره
        ball.bounce_y()

    elif (ball.xcor() > 330 and ball.distance(R_player)<=60) or (ball.xcor() < -330 and ball.distance(L_player)<=60):#زياده سرعه الكره في حاله استمرار اللعب
        speed*=0.8
        ball.bounce_x()

    elif ball.xcor() > 390: # زياده نقاط اللاعب الايسر
        ball.bounce_x()
        time.sleep(1)
        score.l_point()
        ball.reset_position()
        time.sleep(2)
        speed=0.05

    elif ball.xcor() < -390:# زياده نقاط اللاعب الايمن
        ball.bounce_x()
        time.sleep(1)
        score.r_point()
        ball.reset_position()
        time.sleep(1)
        speed=0.05
    
    window.update()





window.exitonclick()