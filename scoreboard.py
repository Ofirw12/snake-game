from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.pencolor('white')
        self.goto(0.0, 260)
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f'Score: {self.score}', False, 'center', ('Courier', 24, 'normal'))

    def update_score(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, 'center', ('Courier', 24, 'normal'))