class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        f = 0
        while True:
            f = nums[f]
            s = nums[s]
            if s == f:
                break

        return s
