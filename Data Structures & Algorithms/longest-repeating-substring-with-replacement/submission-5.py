class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        d = collections.defaultdict(int)
        for r, c in enumerate(s):
            d[c] += 1
            maxf = max(d.values())
            while r-l+1 > maxf + k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len