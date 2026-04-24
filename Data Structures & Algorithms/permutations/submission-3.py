class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, res):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr, res)
                    curr.pop()

        res = []
        backtrack(nums, [], res)
        return res