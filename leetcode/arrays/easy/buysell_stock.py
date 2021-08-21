# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
    INPUTS/OUPUTS
        prices = [7, 1, 5, 3, 6, 4] => 5
        buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

    NOTES
        use a buy_pointer and sell_pointer
        we can use fast/slow pointers so our sell pointer is never before we buy to handle the constraint
"""


def maxProfit(prices):
    max_num = 0
    min_num = float("inf")

    for idx in range(len(prices)):
        current_price = prices[idx]
        if current_price < min_num:
            min_num = current_price
            print('first min', min_num)
        else:
            max_num = max(max_num, current_price - min_num)
            print('max    ', max_num)

    print(max_num)
    return max_num


maxProfit([7, 1, 5, 3, 6, 4])
