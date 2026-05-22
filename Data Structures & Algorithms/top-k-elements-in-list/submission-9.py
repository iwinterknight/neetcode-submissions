class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int)
        for num in nums:
            freqs[num] += 1
        import heapq
        h = []
        for num, freq in freqs.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)
        h = list(map(lambda x: x[1], h))
        return h