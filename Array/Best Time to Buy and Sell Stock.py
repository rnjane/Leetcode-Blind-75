"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
import math
class Solution:
    """
    - profit for each day can be calculated as the difference between the day's price and the minimum price so far.
    - we init min_price to math.inf
    - we loop through all the prices checking if the current price is less than the min_price so far, and if it is,
        we update accordingly.
    - if price is not less than min price, and the current profit is more than current max profit, we re-assign max profit.
    - return max profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
