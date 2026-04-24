class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def recursion(i):
            if i >= n-1:
                return True
            if nums[i] == 0:
                return False

            for step in range(1, nums[i]+1):
                if recursion(i + step):
                    return True
            
            return False

        def memoization(i, cache=None):
            if cache is None:
                cache = {}
            if i in cache:
                return cache[i]
            if i >= n-1:
                return True
            if nums[i] == 0:
                return False

            for step in range(1, nums[i]+1):
                if memoization(i + step, cache):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        # return recursion(0)
        return memoization(0)