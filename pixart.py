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

#Part 1
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

def draw_line_from_string(color_string, turta):
    """
    This function draws one column of pixels based on a color string 
    """
    l = len(color_string)
    s = 1
    for i in color_string:
            m=color_string.index(i)
            int(m)
            color=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
            if i not in color: #Checks if current character is in the list and if it is not it return False
                return False
            else:
                draw_pixel(i, turta)
                if s < l: 
                    if color_string[m+1] not in color:
                        break
                    else:
                        turta.forward(PIXEL_SIZE)
            s= s+1
            m= m+1
    return True #returns True if all characters are valid

def draw_shape_from_string(turta):
    """
    This functions prompts the user to input color string
    """
    while True: #As long as the loop doesnt break, the program will keep asking the user to input more color strings and draw columns
        color_string= input("Please enter colors string: ")
        if color_string == "":
            print("Empty string")
            break #Loop terminates
        else:
            result = draw_line_from_string(color_string, turta)
            if result == False:
                print("Invalid character")
                break #Loop terminates
        turta.penup() #Positioning turtle to next column
        turta.backward((len(color_string)-1)* (PIXEL_SIZE))
        turta.right(90)
        turta.forward(PIXEL_SIZE)
        turta.left(90)
        turta.pendown()
draw_shape_from_string(turta)
#Part 2
def draw_grid(turta):
    """
    This function draws a 20x20 checkered grid of pixels
    """
    for i in range(ROWS):
        turta.speed(0)
        for j in range(COLUMNS):
            if (i + j) % 2 == 0:
                color_string = '0'
            else:
                color_string = '2'
            draw_pixel(color_string, turta)
            if j < COLUMNS-1:
             turta.forward(PIXEL_SIZE)
        turta.penup()
        turta.backward(PIXEL_SIZE * (COLUMNS-1))
        turta.right(90)
        turta.forward(PIXEL_SIZE)
        turta.left(90)
        turta.pendown()
#Part 3
def draw_shape_from_file(turta):
    """
    This function reads from a file and draws a shape based on character sequence. Every line will be
    """
    file_path = input("Enter the path of the file that you want to read its content: ")
    with open(file_path, 'r') as file: #opening the file
        for line in file:
            color = line.strip()
            draw_line_from_string(color, turta) 
            """
            The loop inside this function will iterate over every characte and store it in the parameter color
            """
            turta.penup() #Positioning turtle to next column
            turta.backward((len(line))* (PIXEL_SIZE) - (PIXEL_SIZE*2))
            turta.right(90)
            turta.forward(PIXEL_SIZE)
            turta.left(90)
            turta.pendown()
            
