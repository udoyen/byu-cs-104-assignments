import turtle
from random import randint

t = turtle.Turtle()
s = turtle.getscreen()
user_response = True


def get_color():
    """function to get color

    Returns:
        int: color number
    """
    color = int(input(f"  What color would you like your polygon to be? \n  {'1-Red': <9}  6-Blue\n  {'2-Orange': <10} 7-Purple\n  {'3-Black': <10} 8-Violet\n  {'4-Green': <10} 9-Gold\n  {'5-Indigo': <10} 10-Cyan\n  11-Rainbow(random)\nChoice?  "))
    while True:
        if 1 <= color <= 11:
            return color
        else:
            color = int(input(f"  What color would you like your polygon to be? \n  {'1-Red': <9}  6-Blue\n  {'2-Orange': <10} 7-Purple\n  {'3-Black': <10} 8-Violet\n  {'4-Green': <10} 9-Gold\n  {'5-Indigo': <10} 10-Cyan\n  11-Rainbow(random)\nChoice?  "))
    
def get_number_of_sides():
    """function to get number of sides for the ploygon

    Returns:
        int: number of sides
    """
    number_of_sides = int(input("How many sides for your polygon?  "))
    while True:
        if 1 <= number_of_sides <= 99:
            return number_of_sides
        else:
            number_of_sides = int(input("How many sides for your polygon?  "))

while user_response:

    color = get_color()
    sides = get_number_of_sides()

    side_length = int(input("What side length will your polygon have?  "))
    ext_angle = 360 / sides
    color_list = ['red', 'orange', 'black', 'green', 'indigo', 'blue', 'purple', 'violet', 'gold', 'cyan']

    for i in range(sides):
        if color < 11:
            t.color(color_list[color - 1])
            t.forward(side_length)
            t.left(ext_angle)
        else:
            t.color(color_list[randint(0, 9)])
            t.forward(side_length)
            t.left(ext_angle)
    

    answer = input("Would you like to draw another polygon? (Y/N): ")
    print()
    if answer.upper() == "N":
        user_response = False
    else:
        s.reset()
