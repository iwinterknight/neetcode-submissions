class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_num, r_num = 1, 1
        l_arr, r_arr = [], []
        n = len(nums)
        for i in range(n):
            l_arr.append(l_num)
            r_arr.append(r_num)
            l_num *= nums[i]
            r_num *= nums[n-i-1]

        res = []
        for i in range(n):
            res.append(l_arr[i] * r_arr[n-i-1])
        
        return res