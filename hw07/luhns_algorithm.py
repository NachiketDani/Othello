# Homework7, Exercise1: Luhn's Algorithm
# Prepared by: Nachiket Dani


def main():
    start_program()


# Ask for user input & validate if number is an integer
def start_program():
    check = False
    while check is False:
        user_num = input("Enter your account number: ")
        try:
            int_user_num = int(user_num)
            user_num_list = list(user_num)
            check = True
        except ValueError:
            print("Enter digits only..Try again!")
    modify_list(user_num_list)


# Begin modifying the list
# Obtain length of the list for function for doubling digits
def modify_list(user_num_list):
    len_user_num_list = len(user_num_list)
    if len_user_num_list % 2 == 0:
        len_user_num_list += 1
        double_the_digits(user_num_list, len_user_num_list)
    else:
        double_the_digits(user_num_list, len_user_num_list)


# Double the digits
def double_the_digits(user_num_list, len_user_num_list):
    digit_str = 0
    for i in range(-2, -len_user_num_list, -2):
        user_num_list[i] = int(user_num_list[i])*2
        if user_num_list[i] > 9:
            digit_str = str(user_num_list[i])
            user_num_list[i] = int(digit_str[0]) + int(digit_str[1])
    mod10_check(user_num_list)


# Check if sum up of modified number digits is divisible by 10
def mod10_check(user_num_list):
    sum = 0
    for i in user_num_list:
        sum += int(i)
    if sum % 10 == 0:
        print("This ID is valid.")
    else:
        print("This ID is not valid!")


main()
