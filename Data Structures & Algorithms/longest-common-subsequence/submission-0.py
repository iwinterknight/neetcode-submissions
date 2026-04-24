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


        return memoization(text1, text2)