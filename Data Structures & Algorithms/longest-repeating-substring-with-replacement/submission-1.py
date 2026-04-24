class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        counts = defaultdict(int)
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_char, max_char_freq = None, 0
            for char, freq in counts.items():
                if freq > max_char_freq:
                    max_char = char
                    max_char_freq = freq
            while r-l+1-max_char_freq > k:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len