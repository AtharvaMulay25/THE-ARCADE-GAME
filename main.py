"""
Created on Thur Jan 26 2023
@author: ATHARVA SUHAS MULAY

"""
#importing all the modules 
import turtle
import time
from paddle import Paddle           #importing Paddle Class from the paddle file
from ball import Ball               #importing Ball Class from the ball file
from scoreboard import Scoreboard   #importing Scoreboard Class from the scoreboard file
from cover_page import CoverPage    #importing CoverPage Class from the cover_page file
screen = turtle.Screen()

def set_Screen():
    """
    This Function does the setup of the screen.
    """
    screen.clear()                          #clearing the entire screen intially
    screen.setup(width= 800 , height=600)   #setting width, height of game window
    screen.bgcolor("black")                 #setting bg color as black
    screen.title("PONG")                    #setting title
    screen.tracer(0)                        #turns off the turtle animation


def displayGame():   
    """
    This function displays the game screen having paddles, scores and the ball
    """
    #Asking for Game Points to be played and validating the points
    points = turtle.textinput("Points To be Played", "Enter Points")
    if(not points):
        frontPage(-75, -250)
        return
    else:
        points = int(points)
        if(points<=0): 
            frontPage(-75, -250)
            return

    # time.sleep(0.2)
    #creating left paddle of green color, right paddle of red color and ball object
    r_paddle = Paddle((350,0), "green") 
    l_paddle = Paddle((-350,0), "red")
    ball = Ball()

    #drawing the top, bottom, left and right walls using scoreboard object and updating the initial score
    Scoreboard().draw_walls()          
    scoreboard = Scoreboard()
    scoreboard.update_score()           
    
    #initially ball has not collided with any of the paddles
    r_paddle_collide = False
    l_paddle_collide = False

    #listening for paddle movements and updating paddle positions
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    while(game_is_on):
       
        screen.update()              #updates the screen after every iteration        
        time.sleep(ball.move_speed) #sets the ball speed by changing the sleep time
        ball.move()                 #moving the ball


        #collision with up and down walls
        if(abs(ball.ycor()) > 270):
            ball.bounce_against_walls()
        

        #detect collision with right paddle 
        r_paddle_collide = ball.check_r_collide(r_paddle.position())
        l_paddle_collide = ball.check_l_collide(l_paddle.position())

        if(r_paddle_collide or l_paddle_collide):
            ball.bounce_against_paddles()
        
        #right paddle miss
        if(ball.xcor() >= 380):
            ball.reset_position()
            scoreboard.r_miss()
            

        #left paddle miss
        if(ball.xcor() <= -380):
            ball.reset_position()
            scoreboard.l_miss()
        
        #some player wins the game
        if(scoreboard.l_score == points or scoreboard.r_score == points):
            print("won")
            set_Screen()
            screen.onclick(frontPage)
            while(game_is_on):  
                scoreboard.game_over()



def frontPage(x, y):
    """
    It displays the frontPage of the game by creating object of CoverPage class 
    and then calling the displayFrontPage() method
    """
    print("first ",game_is_on)
    if(x>=-75 and x<=75 and y>=-250 and y<=-210):
        set_Screen()
        #turtle.colormode(255)              #can set customised bg color of the front page
        # screen.bgcolor(251, 255, 25)
        screen.onclick(nextPage)            #displays the next page accordingly if player clicks on the some button 
        cover_page = CoverPage()
        while(game_is_on):                  #displaying the FrontPage continuosly
            print(game_is_on)
            screen.update()
            time.sleep(0.3)
            cover_page.displayFrontPage()
    

def nextPage(x,y):
        """
        It displays the next page depending on the button upon which the player has clicked.
        It either displays the game, or displays the help page or exit the game accordingly
        """
        global game_is_on                   #so that global variable game_is_on can be modified

        #checks if the player has clicked on the Play button
        if(x>=-50 and x<=50 and y>=-80 and y<=-40):
            print("play")        
            set_Screen()
            displayGame()                   #displaying the main game page
       
        #checks if the player has clicked on the Help button
        elif(x>=-50 and x<=50 and y>=-150 and y<=-110):
            print("help")
            set_Screen()
            screen.onclick(frontPage)           #displays the front page if player clicks on the return button
            while(game_is_on):                  #displaying the helpPage continuosly
                cover_page = CoverPage()
                cover_page.helpPage()
           
        
        #checks if the player has clicked on the Exit button
        elif(x>=-50 and x<=50 and y>=-220 and y<=-180):
            print("exit")
            game_is_on = False                  #exits the game


if(__name__ == '__main__'):
    
    game_is_on = True     # a global varible which controls the game state as on/off
    frontPage(-75,-250)   #allowing the front page to be displayed initially 
