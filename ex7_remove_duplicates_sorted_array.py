from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
    :param nums: List of integers
    :return: Number of unique elements in nums
    """
    if not nums:
        return 0  # If the list is empty, return 0

    i = 0  # Initialize the first pointer

    for j in range(1, len(nums)):  # Iterate through the list starting from the second element
        if nums[j] != nums[i]:  # If the current element is different from the last unique element
            i += 1  # Move the first pointer to the next position
            nums[i] = nums[j]  # Update the position with the current unique element

    return i + 1  # Return the number of unique elements


def test_remove_duplicates_from_sorted_array():
    assert remove_duplicates_from_sorted_array([1, 1, 2]) == 2
    assert remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_duplicates_from_sorted_array([]) == 0


if __name__ == '__main__':
    try:
        test_remove_duplicates_from_sorted_array()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")
