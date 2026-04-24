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

        return recursion(0)