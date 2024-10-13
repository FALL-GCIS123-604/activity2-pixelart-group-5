#Layan Zafer and Joudi Alkordi
from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'
#Creating a turtle object
turta= Turtle()

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(character):
    """ 
    Takes character as parameter and returns corresponding color
    """
    if character == '0':
        return "black"
    elif character == '1':
        return "white"
    elif character == '2':
        return "red"
    elif character == '3':
        return "yellow"
    elif character == '4':
        return "orange"
    elif character == '5':
        return "green"
    elif character == '6':
        return "yellowgreen"
    elif character == '7':
        return "sienna"
    elif character == '8':
        return "tan"
    elif character == '9':
        return "gray"
    elif character == 'A':
        return "darkgray"
    else:
        return None

def draw_color_pixel(color_string, turta):
    """
    Drawing one pixel
    """
    turta.fillcolor(color_string)
    turta.begin_fill()
    for i in range(4):
        turta.right(90)
        turta.forward(PIXEL_SIZE)
    turta.end_fill()

def draw_pixel(color_string, turta):
    """
    Draws a pixel corresponding to character color
    """
    color_string= get_color(color_string)
    draw_color_pixel(color_string, turta)