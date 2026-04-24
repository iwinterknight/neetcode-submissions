class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def recursion(i, steps, min_steps=float('inf')):
            if i == n-1:
                return steps
            if i > n-1:
                return float('inf')

            if nums[i] == 0:
                return float('inf')

            for step in range(1, nums[i]+1):
                min_steps = min(min_steps, recursion(i + step, steps + 1, min_steps))
            
            return min_steps


        return recursion(0, 0)