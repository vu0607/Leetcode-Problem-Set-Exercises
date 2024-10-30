def find_index_first_occurrence_in_string(haystack: str, needle: str) -> int:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    :param haystack: The string to search in
    :param needle: The substring to search for
    :return: The index of the first occurrence of needle in haystack, or -1 if not found
    """
    return haystack.find(needle)


def test_find_index_first_occurrence_in_string():
    assert find_index_first_occurrence_in_string(haystack="sadbutsad", needle="sad") == 0
    assert find_index_first_occurrence_in_string(haystack="leetcode", needle="leeto") == -1

if __name__ == '__main__':
    try:
        test_find_index_first_occurrence_in_string()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")