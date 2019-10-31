from bracket_match import BracketMatch


def test_brackets_match():
    """
    Test brackets_match method
    """
    bracket_tester = BracketMatch()
    assert bracket_tester.brackets_match("()") is True
    assert bracket_tester.brackets_match("a(a[a])a({a})") is True
    assert bracket_tester.brackets_match("(") is False
    assert bracket_tester.brackets_match("(}") is False
    assert bracket_tester.brackets_match("a(a(a)a(a)") is False
    assert bracket_tester.brackets_match("aa(a))a(a)") is False
