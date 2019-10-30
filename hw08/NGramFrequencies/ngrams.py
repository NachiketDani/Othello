import sys
from textcleaner import TextCleaner
from frequencies import NgramFrequencies
# from frequencies import NgramFrequencies


def main(filename):
    N_GRAMS_TODO = 3
    N_GRAM_ITERATOR = 1
    try:
        file_object = open(filename)
    except FileNotFoundError:
        print("File", filename, "not found. Try again!")
        return

    text_to_clean = TextCleaner(file_object)
    text_to_clean.preformat()
    sentences = text_to_clean.sentences()

    # Create an NgramFrequencies object
    ngram_result = NgramFrequencies(sentences)
    ngram_result.build_ngram_dict()
    print(ngram_result.top_n_freqs(10))


main(sys.argv[1])
