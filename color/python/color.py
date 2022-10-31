#!/usr/local/bin/python3

#Calculate a complement color from a supplied 24bit color.
#Copyright 2022. thomas.cherry@gmail.com

"""
Calculate the compliment color from a given color
"""

# ##############################################################################
# Terminal Functions

def as_color(color, text):
    """
    Add terminal color codes around text.
    Parameters:
    * color: Array of at least 3 items containing a number from 0-255 for
        Red, Green and Blue
    * text: content to colorize
    """
    red = color[0]
    green = color[1]
    blue = color[2]
    return f"\033[38;2;{red};{green};{blue}m{text}\033[00m"

def expand_color_text(colors):
    """
    Expand a color to a text representation with a box in front showing the
    color. Uses three Unicode glyphs to draw a box.
    """
    box = as_color(colors, "\uEE03\uEE04\uEE05")
    red = colors[0]
    green = colors[1]
    blue = colors[2]
    return f"{box} ({red},{green},{blue}) 0x{red:02x}{green:02x}{blue:02x}"

# ##############################################################################
# Task Functions

def color_limits(value):
    """ Make sure that a supplied value in the byte range of 0-255 """
    if value>255:
        value = 255
    elif value < 0:
        value = 0
    return value

def ask_for_numbers():
    """
    Ask the user for three numbers and return them as an array in RGB order
    Return: [Red, Green, Blue]
    """
    print ('Enter in three values from 0 to 255:\n')
    red = color_limits(int(input("Red> ")))
    green = color_limits(int(input("Green> ")))
    blue = color_limits(int(input("Blue> ")))
    return [red, green, blue]

def find_compliment(color):
    """
    Calculate the color compliment from a supplied color array
    Return: [Red, Green, Blue]
    """
    red = 255-color[0]
    green = 255-color[1]
    blue = 255-color[2]
    return [red, green, blue]

def example_line(color):
    """
    Show one example color displaying the source color and the complement color
    expanded out to text showing the codes and a colored box.
    Return: text with terminal codes and unicode
    """
    compliment = find_compliment(color)
    return f"{expand_color_text(color)}->{expand_color_text(compliment)}"

# ##############################################################################
# Application Functions

def run():
    """ Do all the tasks for this application """
    colors = ask_for_numbers()
    print (example_line(colors))

# Magic python code to respond as a command
if __name__ == '__main__':
    run()
