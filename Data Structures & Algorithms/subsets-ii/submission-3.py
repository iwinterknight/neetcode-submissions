class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def recursion(i=0, curr=[]):
            if i == len(nums):
                res.append(curr[:])
                return

            val = nums[i]
            recursion(i+1, curr + [val])

            j = i+1
            while j < len(nums) and nums[j] == val:
                j += 1
            recursion(j, curr)


        recursion()
        return res