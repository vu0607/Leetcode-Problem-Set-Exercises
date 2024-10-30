from typing import List


def search_insert_position(nums: List[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    :param nums: List of sorted distinct integers
    :param target: Target value to search for
    :return: Index of the target if found, or the index where it would be inserted
    """
    left, right = 0, len(nums) - 1  # Initialize the left and right pointers

    while left <= right:  # Continue the loop until the pointers cross
        mid = (left + right) // 2  # Calculate the middle index
        if nums[mid] == target:  # If the middle element is the target, return its index
            return mid
        elif nums[mid] < target:  # If the middle element is less than the target, move the left pointer to mid + 1
            left = mid + 1
        else:  # If the middle element is greater than the target, move the right pointer to mid - 1
            right = mid - 1

    return left  # If the target is not found, return the insertion point


def test_search_insert_position():
    assert search_insert_position([1, 3, 5, 6], 5) == 2
    assert search_insert_position([1, 3, 5, 6], 2) == 1
    assert search_insert_position([1, 3, 5, 6], 7) == 4


if __name__ == '__main__':
    try:
        test_search_insert_position()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")