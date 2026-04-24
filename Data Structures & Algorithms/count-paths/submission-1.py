class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def memoization(m, n, i, j, cache={}):
            if i == m or j == n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if i == m-1 and j == n-1:
                return 1

            cache[(i, j)] = memoization(m, n, i+1, j, cache) + memoization(m, n, i, j+1, cache)
            return cache[(i, j)]


        def dp(m, n):
            d = [0] * n
            d[-1] = 1
            prevRow = [0] * n
            for r in range(m-1, -1, -1):
                for c in range(n-1, -1, -1):
                    if c+1 < n:
                        d[c] = prevRow[c] + d[c+1]
                prevRow = d
            return d[0]


        # return memoization(m, n, 0, 0)
        return dp(m, n)