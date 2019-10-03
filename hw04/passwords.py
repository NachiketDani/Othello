# Name: Nachiket Dani
# Following code helps generate for the user: a username and 3 password options
# Password options are generated on a predetermined criteria

import random


def main():

    # Welcome User and prompt user to enter their name and favorite word
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name:").lower()
    last_name = input("Please enter your last name:").lower()
    fav_word = input("Please enter your favorite word:").lower()

    # Code piece for creating Username
    """Username created by concatenating first alphabet of first name with
    a string created from the last name such that only 7 characters are always
    printed from that string.If the last name has less than 7 characters, the
    rest should be '*'.Ends with a random integer between 0 and 99"""
    last_name2 = last_name + ("*******")
    username = first_name[0] + last_name2[0:7] + str(random.randint(0, 99))
    print("\nThanks " + first_name.title() + \n
          ", your username is", username, "\n")

    # Code piece for password option 1
    """Password1 is the concatenation of the user's first and last
    names,in lower case, with a random integer in the range 0 – 99 between them
    a,o,l and s in the first and last name are replaced with @,0,1 and $"""
    password1 = first_name + str(random.randint(0, 99)) + last_name
    password1 = password1.replace("a", "@")
    password1 = password1.replace("o", "0")
    password1 = password1.replace("l", "1")
    password1 = password1.replace("s", "$")

    # Code piece for password option 2
    """Password2 is is an "acronym", consisting of the first and last
    character from the user's first name, the first and last character of their
     last name, and the first and last letter of their favorite word.
    In each case, the first letter of the pair should be lower case and the
    second should be upper case"""
    password2 = first_name[0] + first_name[-1].upper() + last_name[0] \
        + last_name[-1].upper() + fav_word[0] + fav_word[-1].upper()

    # Code piece for password option 3
    """The third password takes a random-length portion of the first name,
    combined with random-length portions of the favorite word and last name
    (in any order)."""
    fn_pass3 = first_name[0: random.randint(1, len(first_name))]
    ln_pass3 = last_name[0: random.randint(1, len(last_name))]
    fw_pass3 = fav_word[0: random.randint(1, len(fav_word))]
    password3 = fn_pass3 + ln_pass3 + fw_pass3

    print("Here are three suggested passwords for you to consider:\n")
    print("Password 1: " + password1)
    print("Password 2: " + password2)
    print("Password 3: " + password3)

main()
