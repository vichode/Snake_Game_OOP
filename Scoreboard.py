from turtle import Turtle

Alignment = "center"
FONT = ("Roboto", 14, "bold")

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align= Alignment, font= FONT)

    def game_over(self):
        self.goto(0, 100)
        self.write("GAME OVER!, press 'space' to restart" , align="center", font= ("san serif", 22, "bold"))

    def increase_score(self):
        self.score +=1
        self.write_score()
