class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, j = 0, 0
        max_so_far, max_sum = 0, float('-inf')
        while j < len(nums):
            max_so_far += nums[j]
            max_sum = max(max_sum, max_so_far)
            while max_so_far < 0 and i <= j:
                max_so_far -= nums[i]
                i += 1  
            j += 1      
        
        return max_sum if len(nums) > 1 else nums[0]