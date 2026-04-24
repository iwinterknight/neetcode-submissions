class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, target, i, curr_sum, curr, res):
            if curr_sum == target:
                res.append(curr[:])
                return

            if i >= len(nums) or curr_sum > target:
                return

            curr_sum += nums[i]
            curr.append(nums[i])
            backtrack(nums, target, i, curr_sum, curr, res)
            curr_sum -= nums[i]
            curr.pop()
            backtrack(nums, target, i+1, curr_sum, curr, res)


        res = []
        backtrack(nums, target, 0, 0, [], res)
        return res