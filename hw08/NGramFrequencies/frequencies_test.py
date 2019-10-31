from frequencies import NgramFrequencies


def test_build_ngram_dict():
    """Test unigram, bigram and trigram cases separately for a random sentence"""
    list_test_sentences = ["COMMA COMMA test test", "why why COMMA want"]

    unigram_test = NgramFrequencies(list_test_sentences, 1)
    unigram_test.build_ngram_dict(1)
    assert "COMMA" in unigram_test.ngram_dict.keys()
    assert "test" in unigram_test.ngram_dict.keys()
    assert "why" in unigram_test.ngram_dict.keys()

    bigram_test = NgramFrequencies(list_test_sentences, 2)
    bigram_test.build_ngram_dict(2)
    assert "COMMA_COMMA" in bigram_test.ngram_dict.keys()
    assert "test_test" in bigram_test.ngram_dict.keys()
    assert "why_why" in bigram_test.ngram_dict.keys()
    assert "test_why" not in bigram_test.ngram_dict.keys()

    trigram_test = NgramFrequencies(list_test_sentences, 3)
    trigram_test.build_ngram_dict(3)
    assert "COMMA_COMMA_test" in trigram_test.ngram_dict.keys()
    assert "COMMA_test_test" in trigram_test.ngram_dict.keys()
    assert "why_why_COMMA" in trigram_test.ngram_dict.keys()
    assert "test_why_why" not in trigram_test.ngram_dict.keys()


def test_add_item():
    """Test addition of an item to the ngram dictionary"""
    filler_list = []
    test_wordset = NgramFrequencies(filler_list, 1)
    test_wordset.add_item("COMMA")
    assert "COMMA" in test_wordset.ngram_dict.keys()


def test_top_n_counts():
    """Test construction and sorting of the ngram dictionary"""
    test_sentences = ["hi COMMA how are you",
                      "hi COMMA how are you doing",
                      "im ok COMMA are you", "i'm good"]
    bigram_test = NgramFrequencies(test_sentences, 2)
    bigram_test.build_ngram_dict(2)
    top5 = bigram_test.top_n_counts(5)
    assert top5[0] == ("are_you", 3)
    assert top5[1] == ("hi_COMMA", 2)
    assert "you_i'm" not in top5
    assert len(top5) == 5


def test_top_n_freqs():
    """Test conversion of ngram dictionary to contain frequencies"""
    test_sentences = ["hi COMMA how are you",
                      "hi COMMA how are you doing",
                      "im ok COMMA are you", "i'm good"]
    bigram_test = NgramFrequencies(test_sentences, 2)
    bigram_test.build_ngram_dict(2)
    top5 = bigram_test.top_n_freqs(5)
    assert top5[0] == ("are_you", 0.214)
    assert top5[1] == ("hi_COMMA", 0.143)
    assert "you_i'm" not in top5
    assert len(top5) == 5
