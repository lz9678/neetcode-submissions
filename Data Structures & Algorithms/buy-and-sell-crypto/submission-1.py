class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # profit = sell - buy (high sell, and low buy)
        min_buy = float('inf') # make it as high as possible before we starts optimization

        for price in prices:
            min_buy = price if price < min_buy else min_buy
            cur_profit = price - min_buy
            max_profit = cur_profit if cur_profit > max_profit else max_profit

        return max_profit

        # time: O(n)
        # space: O(1)
