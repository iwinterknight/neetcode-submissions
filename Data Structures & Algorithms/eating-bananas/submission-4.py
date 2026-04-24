class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m, M = 1, max(piles)

        def calculate_time(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total

        def search():
            l, r = m, M
            res = None
            while l <= r:
                rate = l + (r-l) // 2
                time = calculate_time(rate)
                if time <= h:
                    res = rate
                    r = rate - 1
                else:
                    l = rate + 1

            return res

        
        return search()
