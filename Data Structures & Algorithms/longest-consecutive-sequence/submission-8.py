class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        max_freq = 0
        for num in sorted(nums):
            print(d)
            if num-1 in d:
                freq = d[num-1]
                freq += 1
                d[num] = freq
            else:
                freq = 1
                d[num] = freq
            max_freq = max(max_freq, freq)

            
        return max_freq