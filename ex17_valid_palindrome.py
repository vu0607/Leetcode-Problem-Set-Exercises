def is_palindrome(s: str) -> bool:
    """
    Given a string s, return true if it is a palindrome, or false otherwise.
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    # Convert the string to lowercase and filter out non-alphanumeric characters
    filtered_chars = [char.lower() for char in s if char.isalnum()]

    # Check if the filtered list of characters is the same forward and backward
    return filtered_chars == filtered_chars[::-1]


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True


if __name__ == '__main__':
    try:
        test_is_palindrome()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")