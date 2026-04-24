class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m, M = 1, max(piles)

        def total_hours(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total

        def recursive(l, r):
            print(l, r)
            if l >= r and total_hours(l) <= h:
                return l
            mid = l + (r-l) // 2
            mid_hours = total_hours(mid)
            if mid_hours > h:
                return recursive(mid+1, r)
            return recursive(l, mid-1)

        return recursive(m, M)