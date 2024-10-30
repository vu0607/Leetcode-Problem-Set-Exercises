def missing_number(nums: list) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

    :param nums: List of distinct integers
    :return: The missing number in the range [0, n]
    """
    n = len(nums)  # The length of the array
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of numbers in the array
    actual_sum = sum(nums)
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum


def test_missing_number():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


if __name__ == '__main__':
    try:
        test_missing_number()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")