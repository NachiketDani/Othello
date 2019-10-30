

class PrimeGenerator:
    """
    Class to generate prime numbers
    """
    def __init__(self):
        self.composite_set = set()
        self.prime_list = []

    def primes_to_max(self, input_num):
        """
        Returns primes between 2 and the argument value
        """
        START_PRIME = 2
        current_num = START_PRIME
        while current_num != input_num:
            if current_num not in self.composite_set:
                self.prime_list.append(current_num)
                for multiplier in range(2, (input_num//current_num)+1):
                    self.composite_set.add(current_num*multiplier)
            current_num += 1
        return self.prime_list
