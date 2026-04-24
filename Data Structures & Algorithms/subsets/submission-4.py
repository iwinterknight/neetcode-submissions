class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []

        def backtrack(i):
            if i == len(nums):
                res.append(arr[:])
                return

            arr.append(nums[i])
            backtrack(i+1)
            arr.pop()
            backtrack(i+1)


        def recursion(i, curr=[]):
            if i == len(nums):
                res.append(curr[:])
                return

            recursion(i+1, curr + [nums[i]])
            recursion(i+1, curr)


        # backtrack(0)
        recursion(0)
        return res