class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def neetcode_approach(nums):
            nums.sort()
            res = []
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]:
                    continue
                l, r = i + 1, len(nums)-1
                sum = 0
                while l < r:
                    sum = num + nums[l] + nums[r]
                    if sum < 0:
                        l += 1
                    elif sum > 0:
                        r -= 1
                    else:
                        res.append([num, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            return res


        def leetcode_approach(nums):
            dups = set()
            res = set()
            for i, num in enumerate(nums):
                if num not in dups:
                    dups.add(num)
                    seen = {}
                    for j in range(i+1, len(nums)):
                        complement = -(num + nums[j])
                        if complement in seen and seen[complement] == i:
                            res.add([num, nums[j], complement])
                        seen[nums[j]] = i
            return list(res)


        return neetcode_approach(nums)
        # return leetcode_approach(nums)