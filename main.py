from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FPS = 10

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Tony Lukas' Snake Game")

snake = Snake()
scoreboard = Scoreboard()
food = Food()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.up,"e")
screen.onkey(snake.down,"Down")
screen.onkey(snake.down,"d")
screen.onkey(snake.left,"Left")
screen.onkey(snake.left,"s")
screen.onkey(snake.right,"Right")
screen.onkey(snake.right,"f")

screen.tracer(0)

game_is_on = True

while game_is_on:

    snake.move()
    time.sleep(1/FPS)
    screen.update()

    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False

    for seg in snake.segments[1:]:
        if seg.distance(snake.head) < 10:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
