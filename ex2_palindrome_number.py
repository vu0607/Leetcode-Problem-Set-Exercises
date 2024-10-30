def palindrome_number(x: int) -> bool:
    """
    Given an integer x, return true if x is a palindrome integer.
    :param x: input integer
    :return: True if x is a palindrome integer, False otherwise
    """
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


def test_palindrome_number():
    assert palindrome_number(121) == True
    assert palindrome_number(-121) == False
    assert palindrome_number(10) == False


if __name__ == "__main__":
    try:
        test_palindrome_number()
    except:
        print("Tests failed.")
    else:
        print("All tests passed.")