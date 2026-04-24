class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def recursive(nums, i, prev=None, l=0):
            if i >= len(nums):
                return l

            if prev is not None and prev == nums[i]-1:
                return recursive(nums, i+1, nums[i], l+1)
            else:
                return max(recursive(nums, i+1, nums[i], 1), 
                    recursive(nums, i+1, prev, l))

        return recursive(sorted(nums), 0)