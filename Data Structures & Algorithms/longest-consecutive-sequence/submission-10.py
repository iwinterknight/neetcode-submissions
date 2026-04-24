class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        lcs = 0
        for num in nums:
            hash_set.add(num)
        
        for num in nums:
            l = 1
            check_num = num
            while check_num in hash_set:
                check_num -= 1
                l += 1
            lcs = max(lcs, l-1)
        return lcs