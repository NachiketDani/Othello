import random


class ListSearcher:
    """Implements several search algorithms"""
    DEFAULT_SIZE = 10

    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.comparisons = 0

    def generate_data(self, ordered=True):
        """Generate a new ordered or unordered list to experiment on"""
        self._list = list(range(self.size))
        if not ordered:
            random.shuffle(self._list)

    def linear_search(self, key):
        """
        Run linear search for key.
        Return the index of the key.
        """
        for i in range(len(self._list)):
            # Count every time the range loops through a member of the list
            self.comparisons += 1
            if self._list[i] == key:
                return i
        return -1

    def binary_search(self, key):
        """
        Run binary search for key.
        Return the index of the key.
        """
        left = 0
        right = len(self._list) - 1
        while(left <= right):
            # Count everytime left and right indexes are
            # compared and condition is fulfilled
            self.comparisons += 1
            mid = int((left+right)/2)
            if key == self._list[mid]:
                # Count comparison in the "if" statement
                self.comparisons += 1
                return mid
            elif key > self._list[mid]:
                left = mid + 1
                # Count comparison again if it "if" fails
                self.comparisons += 1
            else:
                right = mid - 1
                # Count comparison again if it "elif" fails
                self.comparisons += 1
        # Count comparison if while condition fails
        self.comparisons += 1
        return -1

    def find_median(self):
        """
        Find the median value in an unsorted list.
        Return the index of the median value in the list.
        """
        for i in range(len(self._list)):
            less_than = 0  # counts numbers less than self._list[i]
            grt_than = 0  # counts numbers greater than self._list[i]
            for j in range(len(self._list)):
                # Count the if comparison
                self.comparisons += 1
                if (self._list[j] < self._list[i]):
                    less_than += 1
                elif (self._list[j] > self._list[i]):
                    # Count the Elif comparison
                    self.comparisons += 1
                    grt_than += 1
                else:
                    # Count possibility list is empty and both if/elif fail
                    self.comparisons += 1

            # If the list has odd length, there is a unique median
            # Count first compare in conditional
            self.comparisons += 1
            if (len(self._list) % 2 == 1 and less_than == grt_than):
                # Count second compare in conditional
                self.comparisons += 1
                return i
            # If the list has even length, there are 2 medians. We
            # return the first one that we come across.
            elif (len(self._list) % 2 == 0 and less_than == grt_than - 1):
                # Count both comparisons in conditional
                self.comparisons += 2
                return i
            else:
                # Count failure of first condition in elif
                self.comparisons += 1
                if len(self._list) % 2 == 0:
                    # Count second comparison in elif condition
                    self.comparisons += 1
        # If the list is empty, no median index will be returned
        return -1

    def reset_comparisons(self):
        """
        Reset comparison count
        """
        self.comparisons = 0
