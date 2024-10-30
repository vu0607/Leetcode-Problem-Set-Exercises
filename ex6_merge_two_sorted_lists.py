def merge_two_sorted_lists(list1: list, list2: list):
    """
    You are given the heads of two sorted linked lists list1 and list2.
    Merge two sorted lists into a single sorted list. The list should be made by splicing together the nodes of the first two lists.
    :param list1: List 1
    :param list2: List 2
    :return: Merged sorted list
    """
    # Create a new list to store the merged list
    merged_list = []
    i = j = 0

    # Iterate through both lists
    while i < len(list1) and j < len(list2):
        # Compare the elements from both lists
        if list1[i] < list2[j]:
            # Add the smaller element to the merged list
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add any remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add any remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def test_merge_two_sorted_lists():
    assert merge_two_sorted_lists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    assert merge_two_sorted_lists([], []) == []
    assert merge_two_sorted_lists([], [0]) == [0]


if __name__ == '__main__':
    try:
        test_merge_two_sorted_lists()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")