class Solution:
    def mySqrt(self, x: int) -> int:
        # greatest element lte
        l, r = 1, x
        while l <= r:
            mid = l + (r-l) // 2
            pdt = mid * mid
            if pdt > x:
                r = mid - 1
            else:
                l = mid + 1
        return l-1
