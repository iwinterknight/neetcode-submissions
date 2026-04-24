class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, i, curr, res):
            if i == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(nums, i+1, curr, res)
            curr.pop()
            backtrack(nums, i+1, curr, res)


        res = []
        backtrack(sorted(nums), 0, [], res)
        return res