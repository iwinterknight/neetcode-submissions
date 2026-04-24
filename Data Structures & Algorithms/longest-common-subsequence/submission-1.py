class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def memoization(t1, t2, i=0, j=0, cache={}):
            if i == len(t1) or j == len(t2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            if t1[i] == t2[j]:
                cache[(i, j)] = 1 + memoization(t1, t2, i+1, j+1)
            else:
                cache[(i, j)] = max(memoization(t1, t2, i+1, j+1), memoization(t1, t2, i+1, j), memoization(t1, t2, i, j+1))
            return cache[(i, j)]


        def dp(t1, t2):
            m, n = len(t1) + 1, len(t2) + 1
            d = [[0] * n for _ in range(m)]
            for i in range(1, m):
                for j in range(1, n):
                    if t1[i-1] == t2[j-1]:
                        d[i][j] = 1 + d[i-1][j-1]
                    else:
                        d[i][j] = max(d[i-1][j], d[i][j-1])
            return d[m-1][n-1]

        # return memoization(text1, text2)
        return dp(text1, text2)