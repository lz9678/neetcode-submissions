class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # buy at the lowest and sell at the highest
        min_buy = float('inf') # assume no optimization
        for i in range(0, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            cur_profit = prices[i] - min_buy
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit

            
        