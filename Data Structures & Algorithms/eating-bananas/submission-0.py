class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def inLimit(speed):
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / speed)
            if num_hours <= h:
                return True
            return False


        def search():
            l, r = 1, max(piles)
            prev = None
            while l <= r:
                mid = (l + r) // 2
                if inLimit(mid):
                    prev = mid
                    r = mid - 1
                else:
                    if prev == mid + 1:
                        return prev
                    l = mid + 1
            return prev


        return search()