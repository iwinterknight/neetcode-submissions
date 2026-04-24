class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        char_dict = defaultdict(int)
        max_len = 0
        while r < len(s):
            char_dict[s[r]] += 1
            while l < r and char_dict.get(s[r], 0) > 1:
                char_dict[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
            
        return max_len