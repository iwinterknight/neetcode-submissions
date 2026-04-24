class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        max_len = 0
        win = set()
        for r in range(n):
            while s[r] in win and l <= r:
                win.remove(s[l])
                l += 1
            win.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len