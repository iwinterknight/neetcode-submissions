class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive(nums, i=0, s1=[], s2=[]):
            if i == len(nums):
                if sum(s1) == sum(s2):
                    return True
                return False

            if recursive(nums, i+1, s1 + [nums[i]], s2) or recursive(nums, i+1, s1, s2 + [nums[i]]):
                return True
            return False


        return recursive(nums)