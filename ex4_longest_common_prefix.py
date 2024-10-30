from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    :param strs: List of strings
    :return: Longest common prefix string
    """
    if not strs:
        return ""

    # Sort the list of strings
    strs.sort()

    # Compare the first and the last string in the sorted list
    first = strs[0]
    last = strs[-1]
    i = 0

    # Find the common prefix between the first and last string
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]


def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog","racecar","car"]) == ""


if __name__ == '__main__':
    try:
        test_longest_common_prefix()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")