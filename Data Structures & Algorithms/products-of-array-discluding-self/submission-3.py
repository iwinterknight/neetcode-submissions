class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lprod, rprod = 1, 1
        larr, rarr = [], []
        for num in nums:
            larr.append(lprod)
            lprod *= num

        for i in range(n-1, -1, -1):
            rarr.append(rprod)
            rprod *= nums[i]

        res = []
        for i in range(n):
            res.append(larr[i] * rarr[n-i-1])

        return res