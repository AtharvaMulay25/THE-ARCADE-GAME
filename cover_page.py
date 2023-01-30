#importing the turtle module
import turtle
Turtle = turtle.Turtle
screen = turtle.Screen()

#CONSTANTS

GAME_NAME = "THE ARCADE GAME" 
GAME_TITLE_COLOR = "brown"
GAME_TITLE_FONT = ("Courier", 60, "normal")
#Instructions are fitting in the set screen size and according to size
#of turtle writing
INSTRUCTIONS = ["1. This is a 2-player Game",
                 "2. One player controls left paddle using ",
                 "W, S key and the other player controls right",
                "paddle using up, down arrow", 
                "3. If any player misses the ball, then opposite", 
                "player gets a point and ball is moved to center",
                "4. Both player's score is shown on their",
                "respective side",
                "5. After every strike of ball with paddle, its",
                "speed increases by bit"]
BTN_FONT = ("Courier", 30, "bold")
BTN_TEXT_COLOR = "brown"
BTN_BGCOLOR = (252, 157, 3)

## 

"""CoverPage is a class which will inherit the properties and methods from the Turtle class.
It mades the turtle to display the front page and Help page of the game.
"""
class CoverPage(Turtle):
    """
        Constructor which sets cover_page as a turtle object with color set to white
        """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        # self.displayFrontPage()
    

    def drawBtn(self, startX, startY, text, btnLen, btnHeight):
        """
        It draws the button using cover_page object of btnLen, btnHeight as length and width of button
        resoectively and writes text inside the button
        """
        turtle.colormode(255)
        self.setheading(0)
        self.width(3)
        self.goto(startX,startY)
        self.color(BTN_TEXT_COLOR, BTN_BGCOLOR)
        self.begin_fill()
        for i in range(2):
            self.forward(btnLen);
            self.right(90);
            self.forward(btnHeight);
            self.right(90);
        self.end_fill()
        self.goto(0,startY-40) #turtle is moved to the bottom of the rectangle drawn since it writes above
        self.write(text, align="center", font=BTN_FONT)
        
    def returnBtn(self, x, y):
        """
        This function draws the return Btn according at the passed position
        """
        #You can also write touch here to continue 
        y+=40           #y=-210
        self.drawBtn(-75,y, "Return", 150, 40)

    def helpPage(self):
        """
        This function displays the Help page by writing all the INSTRUCTIONS
         and displaying the return button at the bottom
        """
        x = 0; y= 250
        turtle.colormode(255)
        self.color((168, 108, 30))
        for instruction in INSTRUCTIONS:
            self.goto(x,y)
            self.write(instruction,align="center", font=("Courier", 20, "normal"))   
            y-=50
        self.returnBtn(x,y)    
    
    def displayFrontPage(self):
        """
        It calls all the required functions to display the very front page of the game 
        """
        self.writeGameTitle()   
        self.playBtn()
        self.helpBtn()
        self.exitBtn()
        
        

    def writeGameTitle(self):
        """
        It writes the game title on the front page of the game
        """  
        self.color(GAME_TITLE_COLOR)
        self.sety(50)
        self.write(GAME_NAME, align="center", font=GAME_TITLE_FONT)   
    
  
        
    def playBtn(self):
        """
        It displays the Play btn on the front page of the game
        """
        self.drawBtn(-50, -40 , "Play", 100, 40)

    def helpBtn(self):
        """
        It displays the Help btn on the front page of the game
        """
        self.drawBtn(-50, -110, "Help", 100, 40)

    
    def exitBtn(self):  
        """
        It displays the Exit btn on the front page of the game
        """
        self.drawBtn(-50, -180, "Exit", 100, 40)
