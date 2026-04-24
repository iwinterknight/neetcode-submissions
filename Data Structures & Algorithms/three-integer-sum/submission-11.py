class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        n = len(nums)
        res = set()
        for i, num in enumerate(nums):
            target = -num
            l, r = i+1, n-1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    res.add((num, nums[l], nums[r]))
                    l, r = l+1, r-1
                elif sum < target:
                    l += 1
                else:
                    r -= 1

        return list(res)