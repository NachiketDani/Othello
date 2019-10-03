# Name: Nachiket Dani
# Following code helps generate the fibonacci sequence with length
# equal to the value of the argument entered

import sys


def main():
    digits = int(sys.argv[1])
    fib_num1 = 0
    fib_num2 = 1
    fib_total = 0
    fib_list = [0, 1]

    # For loop through range (digits-2) since we
    # consider 0 and 1 are already part of the sequence
    for i in range(digits-2):
        fib_total = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_total
        fib_list.append(fib_total)

    # Print Fibonacci sequence list
    print(fib_list)

main()
