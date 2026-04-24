class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            n = len(sub)
            if n % 2:
                i, j = n // 2, n // 2
                while i >= 0 and j < n:
                    if sub[i] != sub[j]:
                        return False
                    i, j = i-1, j+1
                if i > 0 or j < n-1:
                    return False
                return True
            else:
                i, j = n // 2 - 1, n // 2
                while i >= 0 and j < n:
                    if sub[i] != sub[j]:
                        return False
                    i, j = i-1, j+1
                if i > 0 or j < n-1:
                    return False
                return True


        def backtrack(s, i, curr, res):
            if i >= len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    curr.append(s[i:j+1])
                    backtrack(s, j+1, curr, res)
                    curr.pop()


        res = []
        backtrack(s, 0, [], res)
        return res