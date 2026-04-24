class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_max, r_max = 0, 0
        n = len(heights)
        l, r = 0, n-1
        l_max_idx, r_max_idx = 0, n-1
        water, max_water = 0, 0
        while l < r:
            if heights[l] > l_max:
                l_max = heights[l]
                l_max_idx = l
            if heights[r] > r_max:
                r_max = heights[r]
                r_max_idx = r
            water = min(l_max, r_max) * (r_max_idx - l_max_idx)
            max_water = max(max_water, water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_water