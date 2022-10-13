from turtle import Turtle,Screen

FONT = ('Hack', 24, 'normal')
SCORE_COLOR = 'green'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color(SCORE_COLOR)
        self.refresh()

    def update_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score}",align='center',font=FONT)

    def game_over(self):
        t = Turtle()
        t.color(SCORE_COLOR)
        t.write("Game Over",font=FONT)

if __name__ == '__main__':
    screen = Screen()

    scoreboard = Scoreboard()
    scoreboard.update_score()
    scoreboard.game_over()
    screen.exitonclick()

