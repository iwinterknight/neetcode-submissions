class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_contained(counts, subcounts):
            for char, freq in subcounts.items():
                if counts.get(char, 0) < freq:
                    return False
            return True
        
        l, r = 0, 0
        subcounts = Counter(t)
        counts = defaultdict(int)
        min_len = float('inf')
        min_str = ""
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while is_contained(counts, subcounts):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_str = s[l:r+1]
                counts[s[l]] -= 1
                l += 1
            r += 1
        return min_str