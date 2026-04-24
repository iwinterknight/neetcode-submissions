class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_contained(counts, subcounts):
            for char, freq in subcounts.items():
                if counts.get(char, 0) < freq:
                    return False
            return True
        
        subcounts = Counter(s1)
        counts = defaultdict(int)
        l, r = 0, 0
        while r < len(s2):
            counts[s2[r]] = 1 + counts.get(s2[r], 0)
            while is_contained(counts, subcounts):
                if r-l+1 == len(s1):
                    return True
                counts[s2[l]] -= 1
                l += 1
            r += 1
        return False
        
        