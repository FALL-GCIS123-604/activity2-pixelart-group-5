#Layan Zafer and Joudi Alkordi Activity 2
from turtle import Screen, Turtle as turta
from pixart import *

def main():
    initialization(turta)
    result=input("What would you like to draw?\n1.Draw shape from string.\n2.Drawcheckers grid.\n3.Draw shape from file.")
    if result == '1':
        draw_shape_from_string(turta)
    elif result == '2':
        draw_grid(turta)
    elif result == '3':
        draw_shape_from_file(turta)
    input("Press any key to exit...")
if __name__ == "__main__":
    main()