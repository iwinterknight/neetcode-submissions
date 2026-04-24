class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        n1 = len(s1)
        l = 0
        counts = defaultdict(int)
        for r in range(len(s2)):
            counts[s2[r]] = 1 + counts.get(s2[r], 0)
            while r-l+1 > n1 and l <= r:
                counts[s2[l]] -= 1
                if counts[s2[l]] == 0:
                    counts.pop(s2[l])
                l += 1
            if counts == c1:
                return True
        return False