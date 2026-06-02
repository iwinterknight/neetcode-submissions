class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculate_time(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time

        def optimize():
            # greatest element lte
            l, r = 1, max(piles)
            while l <= r:
                mid = l + (r-l) // 2
                time = calculate_time(mid)
                if time <= h:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        return optimize()