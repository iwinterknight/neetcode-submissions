class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, i, curr, res):
            if i == len(nums):
                res.append(curr[:])
                return

            recursive(nums, i+1, curr+[nums[i]], res)
            recursive(nums, i+1, curr, res)


        res = []
        recursive(nums, 0, [], res)
        return res