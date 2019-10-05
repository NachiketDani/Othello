# Lab05 Prepared by Nachiket Dani
import re


def main():

    # Obtain file from user
    filename = input("Enter the file name: ")
    try:
        user_file = open(filename, "r")
    except:
        print("Can't open", filename)
        return

    # Code to run count as required
    """
    Declare variables that represent:
    1. count of words
    2. count of characters
    3. count of alphanumeric characters
    """
    word_count = 0
    char_count = 0
    alpha_count = 0
    for line in user_file:
        """Count words by splitting line into list of words"""
        word_count += len(line.split())
        """Count characters by removing all spaces to create line strings"""
        space_rem = line.strip().replace(" ", "")
        char_count += len(space_rem)
        """Count alphanumerics using the regex.findall expression"""
        alpha_count += len(re.findall(r"\w", line))

    print("Words:", word_count)
    print("Characters:", char_count)
    print("Letters & numbers:", alpha_count)
main()
