# Lab02 | Nachiket Dani
#############################################################################################################################
# Write a program that calculates the Euclidean distance between 2 points
def main():
    import math
    x1 = input("What is the x co-ordinate for Point1 ?:")
    y1 = input("What is the y co-ordinate for Point1 ?:")
    x2 = input("What is the x co-ordinate for Point2 ?:")
    y2 = input("What is the y co-ordinate for Point2 ?:")

    # Convert to float & Calculate X and Y coordinate difference squares
    xdistancesq = (int(x1) - int(x2))**2
    ydistancesq = (int(y1) - int(y2))**2

    # Take square root to find Euclidean distance between the 2 points
    p1p2dist = round(math.sqrt(xdistancesq + ydistancesq),2)
    print("The Euclidean distance between the 2 points is:",p1p2dist)
main()