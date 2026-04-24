class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = float('inf')
        bought = None
        max_profit = 0
        for i, price in enumerate(prices):
            if price < min_cost:
                bought = i
                min_cost = price
            if bought is not None and i > bought:
                max_profit = max(max_profit, price - min_cost)
        return max_profit
