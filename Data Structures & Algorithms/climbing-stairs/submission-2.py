class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n, cache={1: 1, 2: 2}):
            if n in cache:
                return cache[n]
            cache[n] = memoization(n-1) + memoization(n-2)
            return cache[n]


        def dp(n):
            tmp = 0
            d = [1, 2]
            if n <= len(d):
                return d[n-1]
            for i in range(2, n):
                tmp = d[0] + d[1]
                d[0] = d[1]
                d[1] = tmp
            return d[1]

        # return memoization(n)
        return dp(n)