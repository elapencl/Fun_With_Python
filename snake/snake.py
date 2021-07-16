from turtle import Turtle


class Snake():
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        self.tail = self.squares[int(len(self.squares))-1]

    def create_snake(self):
        position_x = 0
        for square in range(3):
            snake = Turtle()
            snake.shape('square')
            snake.color('white')
            snake.speed('fastest')
            snake.penup()
            snake.goto(position_x, 0)
            position_x -= 20
            self.squares.append(snake)

    def move_snake(self):
        for index in range(len(self.squares)-1, 0, -1):
            position_x = self.squares[index-1].xcor()
            position_y = self.squares[index-1].ycor()
            self.squares[index].goto(position_x, position_y)
        self.head.forward(20)


    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_square(self):
        position_x = self.squares[int(len(self.squares))-1].xcor()
        position_y = self.squares[int(len(self.squares))-1].ycor()
        square = Turtle()
        square.penup()
        square.shape('square')
        square.color('white')
        square.speed('fastest')
        square.setposition(position_x, position_y)
        self.squares.append(square)
