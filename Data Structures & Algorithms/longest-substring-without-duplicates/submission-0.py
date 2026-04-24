class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        window = {}
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len