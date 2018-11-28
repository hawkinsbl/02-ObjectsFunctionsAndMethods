"""
This module lets you practice correcting SYNTAX (notation) errors.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ben Hawkins.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.
#   Locate the syntax (notation) errors in this file
#   by looking for red underlines.
#
#   For each error, try to make sense of its message.
#     -- Hover and/or expand as needed -- make sure you see the message!
#
#   Then fix the errors, one by one.  IMPORTANT:
#     -- Fixing one error may bring up additional errors
#          (after a few seconds or when you run or save the module).
#     -- Each time, fix the error that is nearest the TOP of the module.
#     -- Often the SOURCE of the error may be on the line
#          just BEFORE the line with a red underline.
#     -- New errors may appear during the RUN of the module.
#
#    Finish by RUNNING the corrected program
#    and making sure that it RUNS CORRECTLY.
#      That is, make sure that (per the doc-strings) the program
#      prints two calculated values and makes a SimpleTurtle do some things.
#
#   When finished, COMMIT-and-PUSH your work, as always.
#
###############################################################################

import rosegraphics as rg
import math

def main():
    """ Calls the other functions in this module to demo them. """
    print_math()
    turtle_fun()


def print_math():
    """ Prints some calculated values. """
    x = math.cos(math.pi)
    print(x)

    y = math.sin(math.pi)
    print("The sine of PI is", y)


def turtle_fun():
    """
    Constructs a TurtleWindow,
    constructs a classic SimpleTurtle and asks it to do some things,
    and waits for the user to click anywhere in the window to close it.
    """
    window = rg.TurtleWindow()
    alan = rg.SimpleTurtle()
    alan.pen = rg.Pen('blue', 30)
    alan.paint_bucket = rg.PaintBucket('yellow')
    alan.backward(3 * (47 + 16))
    alan.begin_fill()
    alan.draw_circle(25)
    alan.end_fill()
    alan.forward(200)
    window.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
