import re


class NgramFrequencies:

    def __init__(self, sentences, n_grams_todo):
        """
        Calculate N-gram Frequencies
        """
        self.n_grams_todo = n_grams_todo
        self.sentences = sentences
        self.ngram_dict = {}
        self.total_count = 0

    def build_ngram_dict(self, n_grams_todo):
        """
        'N'-gram word builder
        """
        for sentence in self.sentences:
            words = re.findall(r"\S+", sentence)
            if self.n_grams_todo == 1:
                for word in words:
                    self.add_item(word)
            elif self.n_grams_todo == 2:
                for i in range(0, len(words) - self.n_grams_todo + 1, 1):
                    wordset = words[i]
                    wordset += "_" + words[i + 1]
                    self.add_item(wordset)
            elif self.n_grams_todo == 3:
                for i in range(0, len(words) - self.n_grams_todo + 1, 1):
                    wordset = words[i]
                    wordset += "_" + words[i + 1] + "_" + words[i + 2]
                    self.add_item(wordset)

    def add_item(self, wordset):
        """
        Takes an n-gram wordset and increments its
        count in the dictionary
        """
        self.total_count += 1
        if wordset in self.ngram_dict.keys():
            self.ngram_dict[wordset] += 1
        else:
            self.ngram_dict[wordset] = 1

    # Below Method is not used but was mentioned in the question
    def top_n_counts(self, n):
        """
        Returns a list of items sorted on the count,
        with the most frequent first
        """
        sorted_unigram_list = sorted(self.ngram_dict.items(),
                                     key=lambda x: x[1], reverse=True)
        return sorted_unigram_list[: n]

    def top_n_freqs(self, n):
        """
        Returns list of frequencies of sorted items
        """
        DECIMAL_PLACES = 3
        unigram_freqs = {key: round(self.ngram_dict[key]/self.total_count,
                         DECIMAL_PLACES) for key in self.ngram_dict.keys()}
        sorted_unigram_freqs = sorted(unigram_freqs.items(),
                                      key=lambda x: x[1], reverse=True)
        return sorted_unigram_freqs[: n]
