def single_number(nums: list) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    :param nums: List of integers where every element appears twice except for one
    :return: The single integer that appears only once
    """
    # Initialize a variable to hold the result of XOR operations
    result = 0

    # Iterate through each number in the array
    for num in nums:
        # XOR the current number with the result
        result ^= num

    # The result will be the single number that appears only once
    return result


def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1


if __name__ == '__main__':
    try:
        test_single_number()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")