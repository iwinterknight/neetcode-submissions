class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_cost = 0, float('inf')
        for i, price in enumerate(prices):
            if price < min_cost:
                min_cost = price
            max_profit = max(max_profit, price-min_cost)
        return max_profit