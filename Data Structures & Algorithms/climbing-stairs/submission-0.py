class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n, cache={1: 1, 2: 2}):
            if n in cache:
                return cache[n]
            cache[n] = memoization(n-1) + memoization(n-2)
            return cache[n]

        return memoization(n) 