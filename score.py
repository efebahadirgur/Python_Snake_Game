from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align='left', font=('Arial', 22, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER!", align = "center", font=('Arial', 22, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()




