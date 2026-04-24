class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(s_counts, t_counts):
            for k, v in t_counts.items():
                if k not in s_counts or s_counts[k] < v:
                    return False
            return True

        l, r = 0, 0
        t_counts = Counter(t)
        s_counts = {}
        min_len = len(s) + 1
        min_win = ""
        while r < len(s):
            s_counts[s[r]] = 1 + s_counts.get(s[r], 0)
            while check(s_counts, t_counts) and l <= r:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_win = s[l:r+1]
                if s[l] in s_counts:
                    s_counts[s[l]] -= 1
                l += 1
            r += 1
        return min_win
            