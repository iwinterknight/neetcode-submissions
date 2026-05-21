class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            seek = target - num
            if seek in d:
                return [d[seek], i]
            d[num] = i
