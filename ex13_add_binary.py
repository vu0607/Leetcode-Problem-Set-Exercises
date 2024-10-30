def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.

    :param a: Binary string
    :param b: Binary string
    :return: Sum of a and b as a binary string
    """
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Add the two integers
    sum_int = int_a + int_b

    # Convert the sum back to a binary string
    return bin(sum_int)[2:]


def test_add_binary():
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"


if __name__ == '__main__':
    try:
        test_add_binary()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")