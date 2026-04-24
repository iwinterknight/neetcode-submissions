class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recursion(i=0, curr=[]):
            if sum(curr) == target:
                res.append(curr[:])
                return

            if i == len(nums) or sum(curr) > target:
                return

            recursion(i, curr + [nums[i]])
            recursion(i+1, curr)

        recursion()
        return res

            
