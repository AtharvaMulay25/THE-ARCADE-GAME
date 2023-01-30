#importing Turtle class from the turtle module
from turtle import Turtle

"""Paddle is a class which will inherit the properties and methods from the Turtle class. """
class Paddle(Turtle):                   
    def __init__(self,position, color): 
        """
        Constructor which sets paddle as a turtle object in the shape of a square streteched accross its width
         with given color and initial position set to given position
        """
        super().__init__()       
        self.shape("square")        
        self.shapesize(stretch_len=1, stretch_wid=5)    
        self.color(color)           
        self.penup()
        self.set_initial_position(position[0],position[1])
    

    def set_initial_position(self,x,y): 
        """
        this function simply sets the paddle object's position to given initial position (x, y)
        """
        self.goto(x,y)

    def go_up(self):  
        """
        go_up() moves the paddle upwards by 40 px
        """    
        self.sety(self.ycor() + 40)
        
    def go_down(self):
        """
        go_down() moves the paddle downwards by 40 px
        """
        self.sety(self.ycor() - 40)
