class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s, e = 0, 0
        max_profit = 0
        while e < len(prices):
            profit = prices[e] - prices[s]
            max_profit = max(max_profit, profit)
            if profit <= 0:
                s = e
            e += 1
        return max_profit