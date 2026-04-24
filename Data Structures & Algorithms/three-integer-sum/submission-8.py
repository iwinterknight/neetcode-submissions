class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i, num in enumerate(nums):
            l, r = 0, len(nums)-1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum == -num and l != i and r != i:
                    res.add(tuple(sorted([num, nums[l], nums[r]])))
                    l, r = l+1, r-1
                elif two_sum < -num:
                    l += 1
                else:
                    r -= 1

        return list(res)
