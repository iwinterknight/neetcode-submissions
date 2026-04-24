class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, i, target, curr, total, res):
            if total == target:
                res.append(curr[:])
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            total += nums[i]
            backtrack(nums, i, target, curr, total, res)
            curr.pop()
            total -= nums[i]
            backtrack(nums, i+1, target, curr, total, res)

        res = []
        backtrack(nums, 0, target, [], 0, res)
        return res