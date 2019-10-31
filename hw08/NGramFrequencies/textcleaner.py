import re


class TextCleaner:

    def __init__(self, file_name):
        """
        Class extracts; returns cleaned lines
        """
        self.file = file_name
        self.clean_text = ""

    def preformat(self):
        """
        Method returns text cleaned of special characters
        & concern for n-gram calc
        """
        chars_dict = {"mr.": "mr", "mrs.": "mrs", "ms.": "ms", ",": " COMMA"}
        for line in self.file:
            line = line.lower()
        # Replace specific characters
            for item in chars_dict.items():
                line = line.replace(item[0], item[1])
        # Remove specific special characters
            line = re.sub(r"[\(\)\"\:\;\-]", "", line)
            self.clean_text += line
        return self.clean_text

    def sentences(self):
        """
        Separates lines from cleaned file text into list of cleaned sentences
        """
        return self.clean_text.split(".")
