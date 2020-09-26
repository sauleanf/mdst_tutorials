from Tutorial1.python_exercises import is_odd
from Tutorial1.python_exercises import is_palindrome
from Tutorial1.python_exercises import only_odds
from Tutorial1.python_exercises import count_words


def test_is_odd_returns_true_if_odd():
    assert is_odd(3)


def test_is_odd_returns_false_if_even():
    assert not is_odd(4)


def test_is_palindrome_with_non_palindrome():
    assert not is_palindrome('abcte')


def test_is_palindrome_with_palindrome_and_even_number():
    assert is_palindrome('abccba')


def test_is_palindrome_with_palindrome_and_odd_number():
    assert is_palindrome('abcba')


def test_only_odds():
    assert only_odds([1, 3, 2, 4, 5, 6]) == [1, 3, 5]


def test_only_odds_with_duplicates():
    assert only_odds([1, 2, 2, 3, 4, 5, 5, 6]) == [1, 3, 5, 5]


def test_count_words():
    test_string = "How much wood would a woodchuck chuck" +\
                    " if a woodchuck could chuck wood?"
    assert count_words(test_string) == {
        'how': 1, 'much': 1, 'wood': 1, 'would': 1,
        'a': 2, 'woodchuck': 2, 'chuck': 2, 'if': 1,
        'could': 1, 'wood?': 1
    }
