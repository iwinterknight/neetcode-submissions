class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        d = collections.defaultdict(int)
        for r, c in enumerate(s):
            d[c] += 1
            max_char, max_char_freq = None, 0
            for char, v in d.items():
                if v > max_char_freq:
                    max_char, max_char_freq = char, v
            while r-l+1 > max_char_freq + k and l <= r:
                d[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len