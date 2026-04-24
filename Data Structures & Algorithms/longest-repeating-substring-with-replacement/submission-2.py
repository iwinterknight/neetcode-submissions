class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        l = 0
        n = len(s)
        max_len = 0
        counts = defaultdict(int)
        for r in range(n):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_char, max_char_freq = None, 0
            for key, val in counts.items():
                if val > max_char_freq:
                    max_char = key
                    max_char_freq = val
            while r-l+1 - max_char_freq > k and l <= r:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len