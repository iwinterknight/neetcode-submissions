class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, res):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(nums, curr, res)
                    curr.pop()
        

        res = []
        backtrack(nums, [], res)
        return res