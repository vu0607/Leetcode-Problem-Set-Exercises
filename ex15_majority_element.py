def majority_element(nums: list) -> int:
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than n / 2 times.
    You may assume that the majority element always exists in the array.

    :param nums: List of integers
    :return: The majority element
    """
    # Initialize the candidate for majority element and a counter
    candidate = None
    count = 0

    # Iterate through each number in the array
    for num in nums:
        if count == 0:
            # Set the current number as the candidate
            candidate = num
        # Increment or decrement the counter
        count += 1 if num == candidate else -1

    return candidate


def test_majority_element():
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


if __name__ == '__main__':
    try:
        test_majority_element()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")