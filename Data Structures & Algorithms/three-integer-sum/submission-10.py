class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    res.add(tuple([num, nums[l], nums[r]]))
                    l, r = l+1, r-1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return list(res)
