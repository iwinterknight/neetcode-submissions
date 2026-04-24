class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_arr, r_arr = [], []
        l_max, r_max = 0, 0
        for h in height:
            l_max = max(l_max, h)
            l_arr.append(l_max)
        for i in range(n):
            r_max = max(r_max, height[n-i-1])
            r_arr.append(r_max)
        
        water = 0
        for i in range(n):
            water += max(min(l_arr[i], r_arr[n-i-1]) - height[i], 0)
        return water