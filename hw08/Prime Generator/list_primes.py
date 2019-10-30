from prime_generator import PrimeGenerator
import sys
import time


def main():
    prime_gen = PrimeGenerator()
    try:
        input_num = int((sys.argv[1]))
    except ValueError:
        print("Enter a valid integer only!")
        return
    # start = time.time()
    print_output(prime_gen.primes_to_max(input_num), input_num)
    # end = time.time()
    # print(end-start, "seconds")


def print_output(numberlist, input_num):
    print("The list of primes from 2 to", input_num, "are:")
    print(numberlist)


main()
