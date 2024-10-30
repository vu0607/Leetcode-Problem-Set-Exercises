from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer,
    increment the large integer by one and return the resulting array of digits.

    :param digits: List of digits representing the large integer
    :return: List of digits representing the incremented large integer
    """
    n = len(digits)  # Get the length of the digits array

    # Iterate over the digits array from the end to the beginning
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:  # If the current digit is less than 9
            digits[i] += 1  # Increment the current digit by 1
            return digits  # Return the result as no further carry is needed
        digits[i] = 0  # If the current digit is 9, set it to 0 and carry over 1 to the next digit

    # If all digits were 9, we need to add an extra 1 at the beginning
    return [1] + digits


def test_plus_one():
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9]) == [1, 0]


if __name__ == '__main__':
    try:
        test_plus_one()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")