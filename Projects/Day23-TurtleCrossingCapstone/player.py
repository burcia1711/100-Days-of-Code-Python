STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.left(90)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        y_cor = self.ycor()
        self.goto(new_x, y_cor)

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        y_cor = self.ycor()
        self.goto(new_x, y_cor)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

