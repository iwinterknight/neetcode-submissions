class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(counts[i][0])
        return res