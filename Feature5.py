def flag_words(S,W):
    """
    This function checks if the word W can be formed by repeating characters in the word S.
    A character repetition is considered significant if it occurs at least 3 times.
    Characters repeated less than 3 times are ignored in the detection process.

    Parameters:
    S (str): The word in which to search for repeated characters.
    W (str): The word to be formed by repeating characters in S.

    Returns:
    bool: True if W can be formed by repeating characters in S, False otherwise.
    """
    # Edge case: None inputs
    if S is None or W is None:
        return False

    # Edge case: both words are the same
    if S == W:
        return False

    # Input validation
    if not isinstance(S, str) or not isinstance(W, str):
        raise ValueError("Both inputs must be strings")

    # Edge case: non-alphabetic characters
    if not S.isalpha() or not W.isalpha():
        return False

    def repeated_letters(s, ind):
        temp = ind
        while temp < len(s) and s[temp] == s[ind]:
            temp += 1
        return temp - ind

    if not S and not W:
        return False

    i, j = 0, 0
    while i < len(S) and j < len(W):
        if S[i] == W[j]:
            len1 = repeated_letters(S, i)
            len2 = repeated_letters(W, j)
            if (len1 < 3 and len1 != len2) or (len1 >= 3 and len1 <= len2):
                return False
            i += len1
            j += len2
        else:
            return False
    return i == len(S) and j == len(W)

import unittest

class TestFlagWords(unittest.TestCase):
    """
    A unittest.TestCase subclass for testing the flag_words function.

    Methods
    -------
    test_flag_words():
    Tests the flag_words function with a variety of different inputs and asserts that the function returns the expected output in each case.
    """
    def test_flag_words(self):
        """
        Tests the flag_words function with a variety of different inputs and asserts that the function returns the expected output in each case.

        The test cases include:
        - A modified word
        - The same word
        - Empty strings
        - Single characters
        - Repeated single character
        - Completely different words

        If any of the assertions fail, the test case will fail, indicating that there is a problem with the flag_words function.
        """
        self.assertTrue(flag_words("mooooronnn", "moron"))  # modified word
        self.assertFalse(flag_words("hello", "hello"))  # same word
        self.assertFalse(flag_words("", ""))  # empty strings
        self.assertFalse(flag_words("a", "a"))  # single characters
        self.assertTrue(flag_words("aaa", "a"))  # repeated single character
        self.assertFalse(flag_words("abc", "def"))  # completely different words