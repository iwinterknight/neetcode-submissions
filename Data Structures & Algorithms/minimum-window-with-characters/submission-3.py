class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if s == t:
            return t
            
        l, r = 0, 0
        t_counts = Counter(t)
        s_counts = {}
        min_len = len(s) + 1
        min_win = ""
        need = len(t)
        have = 0
        while r < len(s):
            s_counts[s[r]] = 1 + s_counts.get(s[r], 0)
            if s[r] in t_counts and s_counts[s[r]] == t_counts[s[r]]:
                have += 1
            while l <= r and have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_win = s[l:r+1]
                s_counts[s[l]] -= 1
                if s[l] in t_counts and s_counts[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return min_win
            