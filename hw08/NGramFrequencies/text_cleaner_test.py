from textcleaner import TextCleaner
import re


def test_preformat_sentences():
    """Test Preformat method"""
    test_file_object = open("floatingisland_wordsworth.txt")
    test_clean1 = TextCleaner(test_file_object)
    test_clean1.preformat()
    test_list = re.findall(r"[\(\)\"\:\;\-]", test_clean1.clean_text)
    assert len(test_list) == 0
    """Test Sentences method"""
    test_list2 = test_clean1.sentences()
    assert len(test_list2) == 4
