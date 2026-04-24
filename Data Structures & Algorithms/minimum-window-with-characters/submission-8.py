class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_contained(d1, d2):
            for k, v in d2.items():
                if d1.get(k, 0) < v:
                    return False
            return True

        n1, n2 = len(s), len(t)
        c2 = Counter(t)
        counts = defaultdict(int)
        l = 0
        min_len = float('inf')
        min_str = ""
        for r in range(n1):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while is_contained(counts, c2) and l <= r:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_str = s[l:r+1]
                counts[s[l]] -= 1
                l += 1
        return min_str