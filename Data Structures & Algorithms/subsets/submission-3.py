class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []

        def recursive(i):
            if i == len(nums):
                res.append(arr[:])
                return

            arr.append(nums[i])
            recursive(i+1)
            arr.pop()
            recursive(i+1)

        recursive(0)
        return res