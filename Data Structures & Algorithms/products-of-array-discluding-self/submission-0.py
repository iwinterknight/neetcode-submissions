class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, reverse = [], []
        for i, num in enumerate(nums):
            if i == 0:
                forward.append(num)
            else:
                forward.append(forward[i-1] * num)

        for i, num in enumerate(nums[::-1]):
            if i == 0:
                reverse.append(num)
            else:
                reverse.append(reverse[i-1] * num)
        
        n = len(nums)
        res = []
        for i in range(n):
            l_pdt, r_pdt = 1, 1
            if i > 0:
                l_pdt = forward[i-1]
            if n-i-1 > 0:
                r_pdt = reverse[n-i-2] 
            res.append(l_pdt * r_pdt)
        return res
        