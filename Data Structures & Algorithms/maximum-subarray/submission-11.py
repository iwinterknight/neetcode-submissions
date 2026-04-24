class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, max_sum = 0, float('-inf')
        for i in range(len(nums)):
            max_so_far += nums[i]
            max_sum = max(max_sum, max_so_far)
            max_so_far = max(max_so_far, 0)
        return max_sum