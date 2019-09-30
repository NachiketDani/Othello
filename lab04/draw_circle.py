# Programming exercise 4: Draw circle

import sys
import math


def main():

    radius = int(sys.argv[1])

    # Defined a function for the distance between 2 points
    # Circle centered at (radius, radius); in the 1st quadrant
    def dist_center(x_traverse, y_traverse):
        return math.sqrt((x_traverse - radius)**2 + (y_traverse - radius)**2)

    # Begin print in top left of the circle
    # Loop through range for x axis upon incrementing y thru range for y axis
    for y in range(2 * radius, -1, -1):
        for x in range(2 * radius):
            if (dist_center(x, y) < radius):
                print("o", end="")
            else:
                print(" ", end="")
        print(" ")

main()
