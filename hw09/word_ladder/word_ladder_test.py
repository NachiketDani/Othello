from word_ladder import WordLadder


# Test function for 2 word pairs
def test_make_ladder():
    """Test for stack size and stack top value"""
    english_words = test_load_words()
    test_dict = {"earth": ["ocean", 14], "wind": ["rain", 5]}
    english_words = test_load_words()
    for testw1, testw2 in test_dict.items():
        test_word = WordLadder(testw1, testw2[0], english_words[len(testw1)])
        test_ladder = test_word.make_ladder()
        assert test_ladder.peek() == testw2[0]
        assert test_ladder.size() == testw2[1]


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
