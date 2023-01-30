#importing the turtle module
import turtle
Turtle = turtle.Turtle

#importing cover_page file for returnBtn function
from cover_page import CoverPage  

#CONSTANTS
LEFT_COLOR = "red"
RIGHT_COLOR = "green"
SCORE_FONT = ("Impact", 60, "normal")

"""Scoreboard is a class which will inherit the properties and methods from the Turtle class."""
class Scoreboard(Turtle):
    def __init__(self):
        """
        Constructor which sets scoreboard as a turtle object, sets the left player's and right
        player's initial score to 0 
        """
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.ht()
        self.penup()
    

    def draw_walls(self):
        """
        This function draws the top, bottom, right, left walls on the game page
        """
        #drawing the top wall with green and red color
        self.width(12)
        self.pencolor("green")
        self.penup()
        self.goto(-394,296)

        self.pendown()
        self.forward(400)
        self.pencolor("red")
        self.forward(400)

        self.goto(390,296)
        self.right(90)

       #drawing the right wall with yellow and red color
        self.forward(300)
        self.pencolor("yellow")
        self.forward(300)


        self.goto(390,-292)
        self.right(90)

        #drawing the top wall with yellow and blue color
        self.forward(400)
        self.pencolor("blue")
        self.forward(400)

        self.goto(-394,-292)
        self.right(90)

        #drawing the top wall with green and blue color
        self.forward(300)
        self.pencolor("green")
        self.forward(300)   
        

    def update_score(self):
        """
        This function updates the score of both the players by first clearing the previous
         scores and then writing the new scores
        """
        
        self.clear()            #to erase both the scores first and then rewrite
        self.goto(-100,200)
        self.color(LEFT_COLOR)
        self.write(self.l_score, align="center", font=SCORE_FONT)
        self.goto(+100,200)
        self.color(RIGHT_COLOR)
        self.write(self.r_score, align="center", font=SCORE_FONT)
    
    def l_miss(self):
        """
        when the left player misses the ball, right gets a point
        """       
        self.r_score+=1
        self.update_score()

    def r_miss(self):  
        """
        when the right player misses the ball, left gets a point
        """      
        self.l_score+=1
        self.update_score()
    
    def game_over(self):
        """
        This function displays the game over page by writing the WIN_MESSAGE,
        LEFT_PLAYER_SCORE, RIGHT_PLAYER_SCORE and displaying the return button
        """
        turtle.colormode(255)
        self.color((168, 108, 30))
        won_player = None
        excess_score = None
        if(self.r_score > self.l_score):
            won_player = "Right"
            excess_score = self.r_score - self.l_score
        else:
             won_player = "Left"
             excess_score = self.l_score - self.r_score

       #displaying the WIN_MESSAGE
        WIN_MESSAGE  = [f"{won_player} Player wins the Game", f"by {excess_score} Points"]
        x=0; y = 50 
        for message in WIN_MESSAGE:
            self.goto(x,y)
            self.write(message, align="center", font=("Calibri", 50, "bold"))
            y-=50
        y-=30    #-80

        #displaying both the scores
        LEFT_PLAYER_SCORE = f"Left Player Score: {self.l_score} Points"
        RIGHT_PLAYER_SCORE = f"Right Player Score: {self.r_score} Points"
        self.color("red")
        self.sety(y)
        self.write(LEFT_PLAYER_SCORE, align="center", font=("Courier", 30, "italic"))
        self.color("green")
        self.sety(y-40)  #-120
        self.write(RIGHT_PLAYER_SCORE, align="center", font=("Courier", 30, "italic"))

        #displaying the return button
        CoverPage().returnBtn(0, -250)   #return btn placed at same position as in help page
