from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        """
        Class for decoding the coded string
        """
        self.decoder_stack = Stack()

    def process_string(self, decode_line):
        """
        Method to decode string using stack
        """
        self.solution_str = ""

        # Check for accidental blank entry
        # Then ensure stack is empty
        if len(decode_line) is 0:
            print("String is empty,try again!")
            return
        else:
            while self.decoder_stack.peek() is not None:
                self.decoder_stack.pop()
        # Loop through encoded string to decode
        for i in decode_line:
            if i == "*":
                if self.decoder_stack.peek() is not None:
                    self.solution_str += self.decoder_stack.pop()
                else:
                    print("Invalid encoded sequence,"
                          "decoded message may not be correct")
                    return self.solution_str
            elif i == "^":
                for j in range(0, 2):
                    if self.decoder_stack.peek() is not None:
                        self.solution_str += self.decoder_stack.pop()
                    else:
                        print("Invalid encoded sequence,"
                              "decoded message may not be correct")
                        return self.solution_str
            else:
                self.decoder_stack.push(i)
        return self.solution_str
