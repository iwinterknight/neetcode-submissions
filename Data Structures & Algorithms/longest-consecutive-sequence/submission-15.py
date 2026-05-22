class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num-1 not in s:
                inc = 0
                while num + inc in s:
                    inc += 1
                res = max(res, inc)
        return res
            