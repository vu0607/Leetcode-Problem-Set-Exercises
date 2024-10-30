def length_of_last_word(s: str) -> int:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.

    :param s: The input string
    :return: The length of the last word in the string
    """
    # Strip any trailing spaces from the string
    s = s.strip()

    # Split the string into a list of words
    words = s.split()

    # Return the length of the last word in the list
    return len(words[-1])


def test_length_of_last_word():
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6


if __name__ == '__main__':
    try:
        test_length_of_last_word()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")