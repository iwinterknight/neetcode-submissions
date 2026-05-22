class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = {v : k for k, v in enumerate(nums)}
        n = len(nums)
        res = set()
        for i in range(n-1):
            for j in range(i+1, n):
                two_sum = nums[i] + nums[j]
                if -two_sum in s and s[-two_sum] not in [i, j]:
                    l = tuple(sorted([nums[i], nums[j], -two_sum]))
                    if l not in res:
                        res.add(l)
        return list(res)