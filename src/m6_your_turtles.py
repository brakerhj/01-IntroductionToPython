"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Haley Braker.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

ryan = rg.SimpleTurtle()
ryan.pen = rg.Pen("pink", 2)
ryan.speed = 2

size = 150
for k in range(3):
    ryan.draw_circle(size)
    ryan.pen_down()
    ryan.forward(k)
    size = size - 10

stella = rg.SimpleTurtle()
stella.pen = rg.Pen('blue', 2)
stella.speed = 4

size = 200
for k in range(3):
    stella.draw_square(size)
    stella.forward(k)
    size = size + 7

window.close_on_mouse_click()
