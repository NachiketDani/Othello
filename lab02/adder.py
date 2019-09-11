# Lab02 | Nachiket Dani
#############################################################################################################################
# Write a program called adder.py which takes input from the user in the form of numerical values, 
# and prints out a sentence reporting the sum of the values
def main():
    First_Value = float(input("Enter a first value:"))
    Second_Value = float(input("Enter a second value:"))
    # Pass and store value into sum variable for future use
    Sum_Value = round( First_Value + Second_Value, 2)
    print ("The sum of ",First_Value,"+",Second_Value," is",Sum_Value)
main()