#!/usr/local/bin/python3

# CopyRight thomas.cherry@gmail.com

"""
Calculate the compliment color from a given color
"""

import os           # get terminal size
import math         # min and max functions
import signal       # force quit handler
import argparse     # command line argument processor

# ##############################################################################
# Terminal Functions

def screen_alt():
    """ Save the screen and display an alternate screen """
    print ("\033[?1049h\033[H")

def screen_clear():
    """ Clear the screen """
    print('\033[2J')  # Clear screen

def screen_restore():
    """ restore the main screen """
    print ("\033[?1049l")

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
    color
    """
    box = as_color(colors, "\uEE03\uEE04\uEE05")
    red = colors[0]
    green = colors[1]
    blue = colors[2]
    return f"{box}{red:02x}{green:02x}{blue:02x}"

# ##############################################################################
# Task Functions

def color_limits(value):
    """ Make sure that a supplied value in the byte range of 0-255 """
    return max(0, min(value, 255))

def ask_for_numbers():
    """ Ask the user for three numbers and return them as an array """
    print ('Enter in three values from 0 to 255:\n')
    red = color_limits(int(input("Red> ")))
    green = color_limits(int(input("Green> ")))
    blue = color_limits(int(input("Blue> ")))
    return [red, green, blue]

def find_compliment(color):
    """ Calculate the color compliment from a supplied color array """
    red = 255-color[0]
    green = 255-color[1]
    blue = 255-color[2]
    return [red, green, blue]

def example_line(color):
    """
    Show one example color displaying the source color and the complement color
    expanded out to text showing the codes and a colored box.
    """
    compliment = find_compliment(color)
    return f"{expand_color_text(color)}->{expand_color_text(compliment)}"

def examples(max_colors):
    """
    Print out a color wheel showing as many colors as can fit on the terminal
    screen.
    """
    print ("Here are some example colors:")
    size = os.get_terminal_size()
    rows = int(256/size.lines)
    cols = int( math.sqrt( (256*256) / size.columns ) +1 )
    for red in range(0, 255, rows):
        for green in range(0, 255, cols):
            for blue in range(0, 255, cols):
                colors = [red, green, blue]
                if max_colors:
                    box = as_color(colors, "\u25a0")
                    print (box, end='')
                else:
                    print (example_line(colors), end="|")
        print ("\n")
    print (f"{size.lines}->{rows}, {256*256}/{size.columns} ->{cols}")

# ##############################################################################
# Application Functions

def initilize_arguments():
    """ Setup the command line argument parser """
    parser = argparse.ArgumentParser()
    # add arguments to the parser
    parser.add_argument("-e", "--examples", action="store_true")
    parser.add_argument("-i", "--interactive", action="store_true")
    parser.add_argument("-m", "--max-colors", action="store_true")
    args = parser.parse_args()
    return args

def force_exit():
    """ A call back function run when the user force quits the application """
    print ("Request to exit now!")

def run():
    """ Do all the tasks for this application """
    args = initilize_arguments()

    if args.interactive:
        screen_alt()

    if args.examples:
        examples(args.max_colors)
    else:
        colors = ask_for_numbers()
        print (example_line(colors))

    if args.interactive:
        input("Press any key to exit.")
        screen_restore()

# Magic python code to respond as a command
if __name__ == '__main__':
    signal.signal(signal.SIGINT, force_exit)
    run()
