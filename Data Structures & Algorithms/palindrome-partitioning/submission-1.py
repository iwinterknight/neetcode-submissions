class Solution:
    import copy
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def palindrome(sub):
            n = len(sub)
            i, j = 0, n-1
            while i <= j:
                if sub[i] != sub[j]:
                    return False
                i, j = i+1, j-1
            return True

        def backtrack(start=0, curr=[]):
            if start == len(s):
                res.append(curr[:])
                return

            for i in range(start, len(s)):
                if palindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(i+1, curr)
                    curr.pop()

        backtrack()
        return res