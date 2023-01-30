#importing Turtle class from the turtle module
from turtle import Turtle

#CONSTANTS
BALL_COLOR = "yellow"

"""Ball is a class which will inherit the properties and methods from the Turtle class. """
class Ball(Turtle):
   
    def __init__(self):
        """
        Constructor which sets ball as a turtle object in the shape of a circle
         with BALL_COLOR as its color and initial position set to given position
        """
        super().__init__()
        self.color(BALL_COLOR)
        self.shape("circle")
        self.penup()
        self.x_move = 10      #ball moves in x-direction by x_move
        self.y_move = 10      #ball moves in y-direction by y_move
        self.move_speed = 0.1 #this changes the sleep time, hence changes the ball speed
        
    def move(self):
        """
        This function moves the ball by increasing its x and y coordinate
         by x_move and y_move respectively
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_against_walls(self):
        """
        It bounces the ball against top and bottom walls by changing its direction in y-axis.
        """
        self.y_move = self.y_move*-1

    def check_r_collide(self, position):
        """
        This function checks for the collision between the ball and the right paddle
        and returns True or False accordingly
        """
        r_paddle_x = position[0]
        r_paddle_y = position[1]
        ball_x = self.xcor()
        ball_y = self.ycor()
        isYcollide = (ball_y <= r_paddle_y + 50)  and  (ball_y >= r_paddle_y -50)
        isXcollide = (ball_x >= r_paddle_x - 20)
        if(isXcollide and isYcollide):
            return True
        return False

    def check_l_collide(self, position):
        """
        This function checks for the collision between the ball and the left paddle
        and returns True or False accordingly
        """
        l_paddle_x = position[0]
        l_paddle_y = position[1]
        ball_x = self.xcor()
        ball_y = self.ycor()
        isYcollide = (ball_y <= l_paddle_y +50)  and  (ball_y >= l_paddle_y -50)
        isXcollide = (ball_x <= l_paddle_x + 20)
        if(isXcollide and isYcollide):
            return True
        return False

    def bounce_against_paddles(self):
        """
        It bounces the ball against left and right paddles by changing its direction in x-axis.
        """
        self.x_move = self.x_move*-1
        self.move_speed*=0.8        #increases speed by 0.8 after every bounce with the paddle

    def reset_position(self):
        """
        It resets the ball's position to center of the screen and its
         speed to original speed
        """
        self.goto(0,0)        
        self.bounce_against_paddles()  #so as to turn the direction to opposite player 
        self.move_speed = 0.1   #setting to original speed


