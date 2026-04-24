class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i > 0 and i < n-1:
                if nums[i-1] >= nums[i] <= nums[i+1]:
                    return nums[i]
        if len(nums) > 1 and nums[-1] < nums[-2]:
            return nums[-1]
        return nums[0]