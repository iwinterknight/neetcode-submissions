class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def recurse(profit, weight, capacity, i):
            if capacity <= 0 or i >= len(profit):
                return 0
            if capacity - weight[i] >= 0:
                return max(profit[i] + recurse(profit, weight, capacity-weight[i], i+1), 
                        recurse(profit, weight, capacity, i+1))
            return recurse(profit, weight, capacity, i+1)


        def memoize(profit, weight, capacity, i=0, cache={}):
            if capacity <= 0 or i >= len(profit):
                return 0
            if (i, capacity) in cache:
                return cache[(i, capacity)]

            if capacity - weight[i] >= 0:
                max_profit = max(profit[i] + memoize(profit, weight, capacity-weight[i], i+1, cache), 
                        memoize(profit, weight, capacity, i+1, cache))
            else:
                max_profit = memoize(profit, weight, capacity, i+1, cache)
            cache[(i, capacity)] = max_profit
            return max_profit


        def dp(profit, weight, capacity):
            D = [[0 for _ in range(capacity+1)] for _ in range(len(profit)+1)]
            for i in range(1, len(D)):
                for j in range(1, len(D[0])):
                    if weight[i-1] <= j:
                        D[i][j] = max(D[i-1][j], profit[i-1] + D[i-1][j-weight[i-1]])
                    else:
                        D[i][j] = D[i-1][j]
            return D[len(profit)][capacity]

        # return recurse(profit, weight, capacity, 0)
        # return memoize(profit, weight, capacity)
        return dp(profit, weight, capacity)