from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
    The relative order of the elements may be changed.
    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    :param nums: List of integers
    :param val: Value to remove
    :return: Number of elements after removing val
    """
    i = 0  # Initialize the first pointer

    for j in range(len(nums)):  # Iterate through the list
        if nums[j] != val:  # If the current element is not equal to the value to remove
            nums[i] = nums[j]  # Update the position with the current element
            i += 1  # Move the first pointer to the next position

    return i  # Return the number of elements after removing val


def test_remove_element():
    assert remove_element([3, 2, 2, 3], 3) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert remove_element([], 0) == 0


if __name__ == '__main__':
    try:
        test_remove_element()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")