class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
        return list(d.keys())[:k]