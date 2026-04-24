class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            prev, next = (i-1)%n, (i+1)%n
            if nums[prev] >= num and num <= nums[next]:
                return num