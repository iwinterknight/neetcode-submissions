class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while True:
            curr, prev, nxt = i % n, (i-1) % n, (i+1) % n
            if nums[curr] <= nums[prev] and nums[curr] <= nums[nxt]:
                return nums[curr]
            i += 1
