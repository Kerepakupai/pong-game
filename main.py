import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


if __name__ == "__main__":
	# Create the screen
	screen = Screen()
	screen.setup(width=800, height=600)
	screen.bgcolor("black")
	screen.title("Pong Game")
	screen.tracer(0)

	r_paddle = Paddle((370, 0))
	l_paddle = Paddle((-370, 0))
	ball = Ball()
	scoreboard = Scoreboard()

# Create and move paddle
	screen.listen()
	screen.onkey(r_paddle.up, "Up")
	screen.onkey(r_paddle.down, "Down")
	screen.onkey(l_paddle.up, "w")
	screen.onkey(l_paddle.down, "s")

	
	is_game_on = True
	while is_game_on:
		time.sleep(ball.move_speed)
		screen.update()
		ball.move()
		# Detect collision with wall and bounce
		if ball.ycor() > 270 or ball.ycor() < -270:
			ball.bounce_y()

		# Detect collision with r_paddle
		if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
			ball.bounce_x()

		# Detect when paddle misses
		if ball.xcor() > 380:
			scoreboard.l_point()
			ball.reset_position()

		if ball.xcor() < -360:
			scoreboard.r_point()
			ball.reset_position()
		
		if scoreboard.l_score > 9 or scoreboard.r_score > 9:
			is_game_on = False


	screen.exitonclick()

