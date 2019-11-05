from word_ladder import WordLadder


# TODO: Write appropriate unit tests

def test_make_ladder():
    test_w1 = earth
    test_w2 = ocean
    english_words = test_load_words()
    test_word = WordLadder(test_w1, test_w2, english_words[len(test_w1)])
    


def test_load_words():
    """Load words from complete wordlist file"""
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


main()
