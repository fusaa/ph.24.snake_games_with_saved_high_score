from turtle import Turtle


class Snake:
    def __init__(self, segments):
        self.segments = 3
        self.PACE = 20
        self.start_pos = 0
        self.body = []
        self.last_direction = 'right'

        for a in range(3):
            self.add_segment()

        self.head = self.body[0]
    #
    # def extend(self):
    #     self.body.append(Turtle())
    #     body[-1].position

    def add_segment(self):
        self.body.append(Turtle())
        self.body[-1].penup()
        self.body[-1].shape("square")
        self.body[-1].shapesize(1, 1, 0)
        self.body[-1].color("white")
        self.body[-1].goto(self.start_pos, 0)
        #self.start_pos -= self.body[-1].position()

    def new_snake(self):
        for a in self.body:
            a.goto(900,900)

        self.body.clear()
        self.last_direction = 'right'

        for a in range(3):
            self.add_segment()

        self.head = self.body[0]





    def move(self,direction):

        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)

        if direction == 'forward':
            self.body[0].forward(20)

    def right(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)
            # self.body[0].forward(20)

    def left(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)
            # self.body[0].forward(20)

    def up(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)
            # self.body[0].forward(20)

    def down(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)
            # self.body[0].forward(20)
