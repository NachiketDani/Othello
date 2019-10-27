import re


class DataAnalysis:

    def __init__(self, file):
        """
        Set up the necessary instance variables
        """
        try:
            self.file = file
            self.languages = {}
            self.country = {}
            self.total_count = 0
            self.read_data(file)
        except FileNotFoundError:
            print("File name not found")
            return

    def read_data(self, file_name):
        """
        Read file,find relevant indices & create dictionaries
        """
        COUNTRY_CODE = 2
        file_object = open(file_name, encoding="utf8")
        first_line = file_object.readline()
        first_line_list = first_line.strip().split(',')
        # Find the columns that the language and email info reside in
        language_index = first_line_list.index("language")
        email_index = first_line_list.index("email")
        # Read the data and get the counts into dictionaries
        # First create Language counts dictionary
        for lines in file_object:
            self.total_count += 1
            language = lines.strip().split(',')[language_index]
            if language in self.languages.keys():
                self.languages[language] += 1
            else:
                self.languages[language] = 1
        # Create the country code counts dictionary
        # Extract the last - '2' length string and count to dictionaries
            email = lines.strip().split(',')[email_index]
            email_end = re.findall(r"\.(\w+)", email)[-1]
            if len(email_end) == COUNTRY_CODE:
                if email_end in self.country.keys():
                    self.country[email_end] += 1
                else:
                    self.country[email_end] = 1

    def sorted_counts(self, collection):
        """
        Sorts dictionaries passed to it in descending order
        """
        return sorted(collection.items(), key=lambda x: x[1], reverse=True)

    def top_n_lang_freqs(self, num):
        """
        Create dictionary: Language counts modified to frequency, sort + return
        """
        self.languages = {key: round(self.languages[key]/self.total_count, 3)
                          for key in self.languages.keys()}
        list_tuples_languages = self.sorted_counts(self.languages)
        return list_tuples_languages[:num]

    def top_n_country_tlds_freqs(self, num):
        """
        Create dictionary: Country counts modified to frequency, sort + return
        """
        self.country = {key: round(self.country[key]/self.total_count, 3)
                        for key in self.country.keys()}
        list_tuples_countries = self.sorted_counts(self.country)
        return list_tuples_countries[:num]
