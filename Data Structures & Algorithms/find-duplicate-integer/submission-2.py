class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) -1
        counts = [0] * n

        for num in nums:
            if counts[num-1] > 0:
                return num
            counts[num-1] += 1
