from turtle import Turtle


class Paddle(Turtle):

	def __init__(self, position) -> None:
		super().__init__()
		self.position = position
		self.shape("square")
		self.color("white")
		self.speed("fastest")
		self.penup()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.goto(position)
	
	def up(self):
			new_y = self.ycor() + 20
			if new_y < 250:
				self.goto(self.xcor(), new_y)

	def down(self):
		new_y = self.ycor() - 20
		if new_y > -250:
			self.goto(self.xcor(), new_y)
