from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.up()
            new_turtle.setx(0 - 20 * i)
            self.segments.append(new_turtle)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.up()
        last_turtle = self.segments[-1]
        pos  = last_turtle.position()
        new_turtle.goto(pos)
        self.segments.append(new_turtle)