# Carry arithmetic program: prepared by Nachiket Dani
def main():
    num_input()


# Function for calling inputs and handling user entry exceptions
def num_input():
    first_num = input("Enter the first number: ")
    try:
        int(first_num)
    except ValueError:
        print("Please enter an integer only!")

    second_num = input("Enter the second number: ")
    try:
        int(second_num)
    except ValueError:
        print("Please enter an integer only")

    sum_function(first_num, second_num)
    list_conversion(first_num, second_num)


# Function to calculate the sum of the 2 integers & print answer
def sum_function(first_num, second_num):
    sum_2nums = int(first_num) + int(second_num)
    print(first_num, "+", second_num, "=", sum_2nums)


# Function to calculate number of carries
def list_conversion(first_num, second_num):
    longest_len = 0
    carry = 0
    carry_count = 0
    ZERO = 0
    first_list = list(first_num)
    second_list = list(second_num)
    """Find the list length difference and add 0s
     to start of shorter list to avoid invalid list indices"""
    len_diff = len(first_list) - len(second_list)
    if len_diff > 0:
        longest_len = -1 * len(first_list)
        for i in range(len_diff):
            second_list.insert(0, ZERO)
    elif len_diff < 0:
        longest_len = -1 * len(second_list)
        for i in range(-len_diff):
            first_list.insert(0, ZERO)
    """Check starting from right most digit if addition leads to a carry"""
    for i in range(-1, longest_len-1, -1):
        if (int(first_list[i]) + int(second_list[i]) + carry) > 9:
            carry = 1
            carry_count += 1
        else:
            carry = 0
    print("Number of carries:", carry_count)


main()
