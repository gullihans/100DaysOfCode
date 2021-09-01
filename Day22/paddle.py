from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, init_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(init_pos)
        self.move = 30

    def go_up(self):
        new_y = self.ycor() + self.move
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move
        self.goto(self.xcor(), new_y)
