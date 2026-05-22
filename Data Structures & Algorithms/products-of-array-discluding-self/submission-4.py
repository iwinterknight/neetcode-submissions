class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr, rarr = [], []
        lprod, rprod = 1, 1
        n = len(nums)
        for i in range(n):
            larr.append(lprod)
            lprod *= nums[i]

        for i in range(n-1, -1, -1):
            rarr.append(rprod)
            rprod *= nums[i]

        res = []
        for i in range(n):
            res.append(larr[i] * rarr[n-i-1])

        return res