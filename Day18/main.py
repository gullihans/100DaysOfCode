import random
import turtle

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


class RandomTurtle(turtle.Turtle):
    def __init__(self, line_width, line_length, turtle_speed):
        super().__init__()
        self.speed(turtle_speed)    # 0 - 10
        self.width(line_width)      # 0 - 10 ???
        self.line_length = line_length
        turtle.colormode(255)
        """ Speed is from 0 to 10, slow to fast"""

    def move(self):
        direction_choice = random.choice([1, 2, 3, 4])
        if direction_choice == 1:
            self.right(0)
            self.forward(self.line_length)
        elif direction_choice == 2:
            self.right(90)
            self.forward(self.line_length)
        elif direction_choice == 3:
            self.right(180)
            self.forward(self.line_length)
        elif direction_choice == 4:
            self.right(270)
            self.forward(self.line_length)

    def turtle_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color((r,g,b))



# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for edge_count in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(edge_count)

tim = RandomTurtle(5,20,10)
tim.shape("circle")
tim.pendown()

while True:
    tim.turtle_color()
    tim.move()

screen = Screen()
screen.exitonclick()
