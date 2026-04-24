class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_max, r_max = [], []
        max_l, max_r = 0, 0
        for height in heights:
            if height > max_l:
                max_l = height
            l_max.append(max_l)
        n = len(heights)
        for i in range(n):
            height = heights[n-i-1]
            if height > max_r:
                max_r = height
            r_max.append(max_r)

        r_max = r_max[::-1]
        max_water = 0
        l, r = 0, n-1
        while l < r:
            water = (r-l) * min(l_max[l], r_max[r])
            if water > max_water:
                max_water = water
            if l_max[l] <= r_max[r]:
                l += 1
            else:
                r -= 1

        return max_water
