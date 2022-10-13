from turtle import Turtle, Screen
import random

class Food(Turtle):

    FOOD_COLOR = 'red'
   
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.color(self.FOOD_COLOR)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)


if __name__ == '__main__':
    screen = Screen()
    food = Food()
    screen.exitonclick()

