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


        # return recursive(nums)
        return memoization(nums)