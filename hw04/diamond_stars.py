# Name: Nachiket Dani
# Following code helps generate a diamond shape made of '*'

"""Special note: If height argument is odd, diamond width is same as height.
If height argument is even the code needs to print a double line of * with
 length as the odd number closest to and lesser than the argument"""

import sys
import math


def main():

    # Declare variables
    blank = " "
    star = "*"
    odd_even = 0
    star_count = 1
    width = 0

    # Take argument as input
    height = int(sys.argv[1])

    # Determine if number entered is odd or even
    if (height % 2) == 0:
        width = (height - 1)
        odd_even = 1
    else:
        width = height
        odd_even = 0
    blank_count = (width//2)

    # Print top part of the diamond
    for i in range(width//2):
        print(blank*blank_count + star*star_count + blank*blank_count)
        blank_count -= 1
        star_count += 2

    # Print a double max width line only if number entered is even
    if odd_even == 1:
        print(star*width)

    # Print bottom part of the diamond from the midline; thus range + 1
    for i in range(width//2 + 1):
        print(blank*blank_count + star*star_count + blank*blank_count)
        blank_count += 1
        star_count -= 2

main()
