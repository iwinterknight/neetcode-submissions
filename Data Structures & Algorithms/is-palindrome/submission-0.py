class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()]).lower()
        n = len(s)
        if n % 2:
            l = r = n // 2
        else:
            l, r = n // 2 - 1, n // 2
        while l >= 0 and r < n:
            if s[l] != s[r]:
                return False
            l, r = l-1, r+1
        if l != -1 and r != n:
            return False
        return True