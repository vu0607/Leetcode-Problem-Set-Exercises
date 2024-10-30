def max_profit(prices: list) -> int:
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day,
    return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    :param prices: List of stock prices
    :return: Maximum profit
    """
    # Initialize the minimum price to a very large value
    min_price = float('inf')
    # Initialize the maximum profit to 0
    max_profit = 0

    # Iterate through each price in the list
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the potential profit if the stock is sold at the current price
        profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if profit > max_profit:
            max_profit = profit

    return max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0


if __name__ == '__main__':
    try:
        test_max_profit()
    except:
        print("Tests failed.")
    else:
        print("All tests passed")