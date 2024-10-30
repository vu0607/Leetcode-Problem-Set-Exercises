def reverse_string(s: list):
    """
    Reverses the input array of characters in-place with O(1) extra memory.

    :param s: List of characters
    :return: None (modifies the input list in-place)
    """
    # Initialize two pointers, one at the beginning and one at the end of the list
    left, right = 0, len(s) - 1

    # Loop until the two pointers meet in the middle
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move the left pointer to the right
        left += 1
        # Move the right pointer to the left
        right -= 1

    return s

def test_reverse_string():
    assert reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert reverse_string(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]


if __name__ == '__main__':
    try:
        test_reverse_string()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")
