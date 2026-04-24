class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def recursive(nums, i, prev=None, l=0):
            if i >= len(nums):
                return l

            if prev is not None and prev == nums[i]-1:
                return recursive(nums, i+1, nums[i], l+1)
            else:
                return max(recursive(nums, i+1, nums[i], 1), 
                    recursive(nums, i+1, prev, l))


        def memoize(nums, i, prev=None, l=0, cache={}):
            if i >= len(nums):
                return l

            if (i, l) in cache:
                return cache[(i, l)]

            if prev is not None and prev == nums[i]-1:
                cache[(i, l)] = memoize(nums, i+1, nums[i], l+1, cache)
                return cache[(i, l)]
            else:
                cache[(i, l)] = max(memoize(nums, i+1, nums[i], 1, cache), 
                    memoize(nums, i+1, prev, l, cache))
                return cache[(i, l)]

        return recursive(sorted(nums), 0)
        # return memoize(sorted(nums), 0)
