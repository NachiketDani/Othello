from prime_generator import PrimeGenerator


def test_primes_to_max():

    # ensure that some known primes are showing up
    # in the appropriate places in the list when
    # the method is called on smaller numbers.
    prime_gen_test = PrimeGenerator()
    assert prime_gen_test.primes_to_max(100) == [2, 3, 5, 7, 11, 13, 17, 19, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
