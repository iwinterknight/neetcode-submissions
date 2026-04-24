class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive(nums, n=len(nums)-1):
            if n < 0:
                return 0

            return max(recursive(nums, n-1), nums[n] + recursive(nums, n-2))


        def memoization(nums, n=len(nums)-1, cache={}):
            if n < 0:
                return 0

            if n in cache:
                return cache[n]

            cache[n] = max(memoization(nums, n-1, cache), nums[n] + memoization(nums, n-2, cache))
            return cache[n]


        def dp(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            d = [nums[0], nums[1]] + [0 for i in range(2, n)]
            for i in range(1, n):
                d[i] = max(d[i-1], nums[i] + d[i-2])
            return d[n-1]


        # return recursive(nums)
        # return memoization(nums)
        return dp(nums)