# # Name: Nachiket Dani
# Following code generates Triangular numbers
"""Code takes value of the argument which is a
 positive integer and prints the sum of values from 1 to that number"""

import sys


def main():

    user_input = int(sys.argv[1])

    sum_num = 0

    while user_input > 0:
        sum_num = sum_num + user_input
        user_input -= 1

    print("The sum of the numbers is", sum_num)


main()
