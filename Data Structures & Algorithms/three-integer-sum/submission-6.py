class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hmap = {}
        for i, num in enumerate(nums):
            hmap[num] = i

        def twoSum(req_sum, exclude_index):
            res = []
            for j, num in enumerate(nums):
                if req_sum - num in hmap and exclude_index != j:
                    lookup_index = hmap[req_sum-num]
                    if lookup_index != exclude_index and lookup_index != j:
                        res.append([num, req_sum-num])
            return res

        final = set()
        for k, num in enumerate(nums):
            two_sum_res = twoSum(-num, k)
            for res in two_sum_res:
                final.add(tuple(sorted([num, res[0], res[1]])))
        
        return list(final)
