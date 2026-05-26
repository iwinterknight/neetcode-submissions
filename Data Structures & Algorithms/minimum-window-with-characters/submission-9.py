class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_contained(d1, d2):
            for k, v in d2.items():
                if d1.get(k, 0) < v:
                    return False
            return True

        tc = Counter(t)
        n, m = len(s), len(t)
        min_len = float('inf')
        min_str = ""
        l = 0
        sc = defaultdict(int)
        for r in range(n):
            sc[s[r]] += 1
            while is_contained(sc, tc) and l <= r:
                sc[s[l]] -= 1
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_str = s[l:r+1]
                l += 1
        return min_str
