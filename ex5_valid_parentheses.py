def valid_parentheses(s: str) -> bool:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    :param s: input string
    :return: True if the input string is valid, False otherwise
    """
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Stack to keep track of opening brackets
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Check the last element in the stack (if it exists), and pop it if it matches the expected opening bracket
            top_element = stack.pop() if stack else ''

            # If the top element doesn't match the corresponding opening bracket, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty at the end, all brackets matched; otherwise, return False
    return not stack


def test_valid_parentheses():
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("([)]") == False
    assert valid_parentheses("{[]}") == True


if __name__ == '__main__':
    try:
        test_valid_parentheses()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")