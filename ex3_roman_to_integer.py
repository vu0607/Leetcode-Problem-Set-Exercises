ROMAN_DICT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(s: str) -> int:
    """
    Given a roman numeral, convert it to an integer.
    :param s: input roman numeral
    :return: equivalent integer
    """

    # Initialize the result to store the final integer value
    result = 0
    # Variable to track the value of the previous Roman numeral
    prev = 0
    for i in s:
        # Check if the current Roman numeral is greater than the previous one
        if ROMAN_DICT[i] > prev:
            # If it is, subtract twice the previous value (because we added it once already)
            # and then add the current value. This handles cases like IV (4) or IX (9).
            result += ROMAN_DICT[i] - 2 * prev
        else:
            # If the current value is not greater, simply add it to the result
            result += ROMAN_DICT[i]

        # Update prev to the current Roman numeral's value for the next loop iteration
        prev = ROMAN_DICT[i]

    # Return the final calculated integer value
    return result


def test_roman_to_integer():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994


if __name__ == "__main__":
    try:
        test_roman_to_integer()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")