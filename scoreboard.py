from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        # self.high_score = 0
        self.load_data()
        self.goto(-60, 280)
        self.message = "Score: " + str(self.score) + " High Score: " + str(self.high_score)
        self.write(self.message)

    def update(self):
        self.score += 1
        self.message = "Score: " + str(self.score) + "   High Score: " + str(self.high_score)
        self.clear()
        self.write(self.message)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER")
    def start_over(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.message = "Score: " + str(self.score) + "   High Score: " + str(self.high_score)
            self.clear()
            self.write(self.message)
        self.write_data()
        self.score = 0
        self.message = "Score: " + str(self.score) + "   High Score: " + str(self.high_score)
        self.clear()
        self.write(self.message)

    def load_data(self):
        with open('data.txt','r') as file:
            self.high_score = int(file.read())
        print(f"high score from file is {self.high_score}")

    def write_data(self):
        with open('data.txt','w') as file:
            file.write(str(self.high_score))









