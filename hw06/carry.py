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
    list_conversion(first_num, second_num)


# Function to calculate number of carries
def list_conversion(first_num, second_num):
    longest_len = 0
    ZERO = 0
    first_list = list(first_num)
    second_list = list(second_num)

    """Find the list length difference and add 0s
     to start of shorter list to avoid invalid list indices"""
    len_diff = len(first_list) - len(second_list)
    if len_diff >= 0:
        longest_len = -1 * len(first_list)
        for i in range(len_diff):
            second_list.insert(0, ZERO)
    elif len_diff < 0:
        longest_len = -1 * len(second_list)
        for i in range(-len_diff):
            first_list.insert(0, ZERO)
    carry_summation(first_num, second_num, first_list,
                    second_list, longest_len)


# Function to calculate sum of numbers using carry arithmetic
def carry_summation(first_num, second_num, first_list,
                    second_list, longest_len):
    carry = 0
    carry_count = 0
    sum_string = ""
    sum_list = []
    for i in range(-1, longest_len - 1, -1):
        """Check starting from right most digit if addition leads to a carry"""
        if (int(first_list[i]) + int(second_list[i]) + carry) > 9:
            """Cast sum of indices into sum string"""
            sum_string = str(int(first_list[i]) + int(second_list[i]) + carry)
            """Insert rightmost digit into sum list"""
            sum_list.insert(0, int(sum_string[-1]))
            carry = 1
            carry_count += 1
        else:
            sum_list.insert(0, (int(first_list[i]) +
                            int(second_list[i]) + carry))
            carry = 0
    """If we have a leftover carry at end of sum, add to sum list"""
    if carry == 1:
        sum_list.insert(0, 1)
    """Re-initiate sum string to help convert sum list to a string"""
    sum_string = ""
    for i in sum_list:
        sum_string += str(i)
    """Print answer"""
    print(first_num, "+", second_num, "=", sum_string)
    print("Number of carries:", carry_count)


main()
