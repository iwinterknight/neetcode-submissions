class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = 1
        
        max_freq = 0
        for num, freq in d.items():
            if d[num] == 1:
                freq  = 0
                next_num = num
                while next_num in d:
                    freq += 1
                    next_num += 1
            max_freq = max(max_freq, freq)

        return max_freq