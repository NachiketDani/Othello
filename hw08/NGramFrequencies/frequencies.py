import re


class NgramFrequencies:

    def __init__(self, sentences):
        """
        Calculate N-gram Frequencies
        """
        # self.n_grams_todo = n_grams_todo
        self.sentences = sentences
        self.unigram = {}
        self.total_count = 0

    def build_ngram_dict(self):
        for sentence in self.sentences:
            words = re.findall(r"\S+", sentence)
            # if (self.n_grams_todo > 1):
            #     for i in range(0, len(words) - self.n, 1):
            #         wordset = words[i]
            #         for j in range(i+1, i + self.n, 1):
            #             wordset += "_" + words[j]
            #         self.add_item(wordset)
            for word in words:
                self.add_item(word)

    def add_item(self, wordset):
        """
        Takes an n-gram and increments its
        count in the dictionary
        """
        self.total_count += 1
        if wordset in self.unigram.keys():
            self.unigram[wordset] += 1
        else:
            self.unigram[wordset] = 1
        # print(self.unigram)

    def top_n_counts(self, n):
        """
        Returns a list of items sorted on the count,
        with the most frequent first
        """
        sorted_unigram_list = sorted(self.unigram.items(),
                                     key=lambda x: x[1], reverse=True)
        return sorted_unigram_list[: 10]

    def top_n_freqs(self, n):
        """
        Returns frequencies of sorted items
        """
        DECIMAL_PLACES = 3
        unigram_freqs = {key: round(self.unigram[key]/self.total_count,
                         DECIMAL_PLACES) for key in self.unigram.keys()}
        # print(unigram_freqs)
        sorted_unigram_freqs = sorted(unigram_freqs.items(),
                                      key=lambda x: x[1], reverse=True)
        return sorted_unigram_freqs[: n]
