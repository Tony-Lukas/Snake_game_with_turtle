from turtle import Turtle,Screen


NUMBER_OF_SEGMENTS = 3
SNAKE_COLOR = "blue"
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_segment()
        self.head = self.segments[0]

    def create_segment(self):
        for i in range(NUMBER_OF_SEGMENTS):
            self.add_segment((-20*i,0))

    def add_segment(self,position):
        seg = Turtle('square')
        seg.penup()
        seg.color(SNAKE_COLOR)
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


if __name__ == '__main__':
    screen = Screen()
    snake = Snake()
    for _ in range(10):
        snake.move()
    screen.exitonclick()
