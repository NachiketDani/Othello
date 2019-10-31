import sys
from textcleaner import TextCleaner
from frequencies import NgramFrequencies
# from frequencies import NgramFrequencies


def main(filename):
    N_GRAMS_TODO = [1, 2, 3]
    TOP_TEN_NGRAMS = 10
    try:
        file_object = open(filename)
    except FileNotFoundError:
        print("File", filename, "not found. Try again!")
        return

    # Class Object created for Text cleaner
    text_to_clean = TextCleaner(file_object)
    # Call the preformat method that returns a cleaned string
    text_to_clean.preformat()
    # Separates the cleaned string into list of sentences
    sentences = text_to_clean.sentences()

    # Class Object created for N grams
    for i in N_GRAMS_TODO:
        ngram_result = NgramFrequencies(sentences, i)
        ngram_result.build_ngram_dict(i)
        if i is 1:
            print("Top", TOP_TEN_NGRAMS, "unigrams:")
        elif i is 2:
            print("\nTop", TOP_TEN_NGRAMS, "bigrams:")
        elif i is 3:
            print("\nTop", TOP_TEN_NGRAMS, "trigrams:")
        print_it(ngram_result.top_n_freqs(TOP_TEN_NGRAMS))


# Print function
def print_it(collection):
    for item in collection:
        print(item)


main(sys.argv[1])
