class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, i, curr, res, counts):
            if i == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return

            if counts[nums[i]] > 0:
                curr.append(nums[i])
                counts[nums[i]] -= 1
                backtrack(nums, i+1, curr, res, counts)
                curr.pop()
                counts[nums[i]] += 1
                backtrack(nums, i+1, curr, res, counts)


        counts = Counter(nums)
        res = []
        backtrack(sorted(nums), 0, [], res, counts)
        return res