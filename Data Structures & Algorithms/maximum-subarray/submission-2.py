class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]
        for num in nums[1:]:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum