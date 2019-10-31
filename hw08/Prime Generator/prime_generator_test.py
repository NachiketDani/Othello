from prime_generator import PrimeGenerator
import random


def test_primes_to_max():

    # Test1: Ensure primes from 1 to 100 match list
    prime_gen_test1 = PrimeGenerator()
    primes_to_100 = [2, 3, 5, 7, 11, 13, 17, 19,
                     23, 29, 31, 37, 41, 43, 47,
                     53, 59, 61, 67, 71, 73, 79,
                     83, 89, 97]
    assert (prime_gen_test1.primes_to_max(100)
            == primes_to_100)

    # Test2: Ensure the 100th prime is 541
    prime_gen_test2 = PrimeGenerator()
    result = prime_gen_test2.primes_to_max(1000)
    assert result[99] == 541
