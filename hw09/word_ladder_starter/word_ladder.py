from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.stack_ladder = Stack()
        self.queue_ladder = Queue()
        self.words_made = {w1}

    def make_ladder(self):
        """
        Create word ladder method W1 to W2
        """
        top_word = ""        # Top word of the stack returned on peek
        change_word = ""     # Ladder word created by changing char
        new_stack = Stack()  # New stack with valid intermediary words
        ladder_size = 0
        alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"}
        # Step1a: Push w1 to stack
        self.stack_ladder.push(self.w1)
        # Step1b: Initialize queue containing stack
        self.queue_ladder.enqueue(self.stack_ladder)
        # Step2a: Dequeue stack then peek top word
        ladder_size = self.queue_ladder.size()
        while self.queue_ladder.size() > 0:
            for member in range(ladder_size):
                stack_removed = self.queue_ladder.dequeue()
                top_word = stack_removed.peek()
                # Step2b: For each char in top word do step2c
                for index in range(len(top_word)):
                    # Step2c: For each letter in the alphabet replace
                    # character with that alphabet to create new word
                    for letter in alphabet:
                        change_word = (top_word[0: index]
                                      + letter + top_word[index + 1:])
                        # print(change_word)
                        # Step2d: Check if new word is a valid English word
                        if (change_word in self.wordlist and
                           change_word not in self.words_made):
                            # Step2e: If valid, copy stack and
                            # Push new word to stack
                            self.words_made.add(change_word)
                            new_stack = stack_removed.copy()
                            new_stack.push(change_word)
                            # print("NewStack", new_stack)
                            # Step2f: If new word is the same as w2
                            # return the new stack
                            if change_word == self.w2:
                                return new_stack
                            else:
                                # Step2g: New word not last word of ladder
                                # Enqueue new stack to the end of the queue
                                self.queue_ladder.enqueue(new_stack)
