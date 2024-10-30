def climb_stairs(n: int) -> int:
    """
    Given a staircase with n steps, return the number of distinct ways to climb to the top.
    Each time you can either climb 1 or 2 steps.

    :param n: Number of steps to reach the top
    :return: Number of distinct ways to climb to the top
    """
    if n == 1:
        return 1  # There is only one way to climb one step

    # Initialize an array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    dp[1] = 1  # There is one way to reach the first step
    dp[2] = 2  # There are two ways to reach the second step

    # Fill the array for steps 3 to n
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # The number of ways to reach step i is the sum of the ways to reach steps i-1 and i-2

    return dp[n]  # The number of ways to reach the top step


def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5


if __name__ == '__main__':
    try:
        test_climb_stairs()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")