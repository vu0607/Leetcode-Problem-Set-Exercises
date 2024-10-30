from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    :param nums: an array of integers
    :param target: the target sum
    :return: indices of the two numbers that add up to the target
    """
    # Create a dictionary to store the index of each number
    num_dict = {}
    for idx, num in enumerate(nums):
        # Check if the difference between the target and the current number is in the dictionary
        if target - num in num_dict:
            # If it is, return the indices of the two numbers
            return [num_dict[target - num], idx]
        # Otherwise, add the current number to the dictionary
        num_dict[num] = idx
    # If no solution is found, return an empty list
    return []


def test_two_sum():
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]


if __name__ == "__main__":
    try:
        test_two_sum()
    except:
        print("Tests failed.")
    else:
        print("All tests passed.")