from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head=self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        tim = Turtle(shape="square")
        tim.color("White")
        tim.penup()
        tim.goto(position)
        self.turtle_list.append(tim)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move(self):
        for seg_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[seg_num - 1].xcor()
            new_y = self.turtle_list[seg_num - 1].ycor()
            self.turtle_list[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.turtle_list:
            seg.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
