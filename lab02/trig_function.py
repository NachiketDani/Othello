# Lab02 | Nachiket Dani
#############################################################################################################################
def main():
    import math
    # Convert the incoming string into a float for using math functions
    deg_angle = float(input("Enter the value of the angle in degrees:"))

    # Use the sine & cosine function in the 'math' library. Since the math.sin & math.cos functions work
    # on radians, we have to convert the angle entered into degrees in order to use it for our program
    sin_angle = math.sin(math.radians(deg_angle))
    cos_angle = math.cos(math.radians(deg_angle))

    print("The sine of",deg_angle,"is:",sin_angle)
    print("The cosine of",deg_angle,"is:",cos_angle)
main()