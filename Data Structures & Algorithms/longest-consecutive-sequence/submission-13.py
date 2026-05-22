class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = sorted(list({v : k for k, v in enumerate(nums)}.items()))
        inc, res = 0, 0
        prev_k, prev_v = None, None
        for k, v in d:
            if prev_k is None or k == prev_k + 1:
                inc += 1
                res = max(res, inc)
            else:
                inc = 1
            prev_k, prev_v = k, v

        return res 