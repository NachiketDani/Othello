# Triangular number list program: prepared by Nachiket Dani


def main():
    input_check()


def input_check():
    done = False
    sum_num = 0
    triangular_ls = []

    while done is False:
        user_input = input("Enter a number, or enter 'done': ")
        if user_input.lower() == "done":
            if len(triangular_ls) > 0:
                print(triangular_ls)
            elif len(triangular_ls) is 0:
                print("No numbers entered! Try again")
            return
        try:
            int(user_input) == int

        except ValueError:
            print("Invalid input! Try Again")
            return
        """Print sum and append the sum to triangular number list"""
        user_input = int(user_input)
        while user_input > 0:
            sum_num = sum_num + user_input
            user_input -= 1
        print("The sum of the numbers is", sum_num)
        triangular_ls.append(sum_num)


main()
