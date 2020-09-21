# ControlP5 is a 3rd party library that gives us
# interface controls. We need it for the slider.
add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider

# Here we import the Point class definition from
# the other tab of this sketch. That file is
# and ordinary .py file stored in the same
# sketch directory.
from point import Point

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


# This code is executed only once, at the beginning
# of your sketch. Conceptually, the setup function has
# a similar role to a class's constructor
def setup():
    size(430, 400)
    noStroke()
    setupSlider()


# The draw method is executed repeatedly, coinciding
# with screen refreshes. Anything that needs to be
# redrawn, recalculated, animated, or to respond to
# user interaction will need to be carried out within the
# draw loop.
def draw():
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


# This is a recursive function that draws the Sierpinski triangle
def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    # Run recursion only if the depth is greater than 0
    if recursionDepth > 0:
        # Calculate midpoints for left, right and bottom lines
        left_midpt = top.midPoint(bottomLeft)
        right_midpt = bottomRight.midPoint(top)
        bottom_midpt = bottomRight.midPoint(bottomLeft)
        # Color black
        fill(0)
        # Draw black triangle
        triangle(left_midpt.xCoord, left_midpt.yCoord,
                 right_midpt.xCoord, right_midpt.yCoord,
                 bottom_midpt.xCoord, bottom_midpt.yCoord)
        # Recursively call function 3 times
        # Each depth splits the main triangle to 3
        sierpinksi(bottomLeft, bottom_midpt, left_midpt, recursionDepth-1)
        sierpinksi(bottom_midpt, bottomRight, right_midpt, recursionDepth-1)
        sierpinksi(left_midpt, right_midpt, top, recursionDepth-1)


# The code below sets up the slider and sets a listener callback
# function to respond to the user sliding the slider.
def setupSlider():
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    global depth
    depth = event.value()
