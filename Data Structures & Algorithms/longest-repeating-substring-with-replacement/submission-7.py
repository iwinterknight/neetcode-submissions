class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len, maxf = 0, 0
        d = collections.defaultdict(int)
        for r, c in enumerate(s):
            d[c] += 1
            maxf = max(maxf, d[c])
            if r-l+1 > maxf + k:
                d[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len