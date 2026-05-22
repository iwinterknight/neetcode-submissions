class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            inc = 1
            while num-1 in s:
                inc += 1
                num = num-1
            res = max(res, inc)
        return res
            