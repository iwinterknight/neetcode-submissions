class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sorting_based(nums, k):
            d = {}
            for num in nums:
                d[num] = 1 + d.get(num, 0)
            d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
            return list(d.keys())[:k]


        def heap_based(nums, k):
            heap = []
            counts = {}
            for num in nums:
                counts[num] = 1 + counts.get(num, 0)
            for num, count in counts.items():
                heap.append((-count, num))
            heapq.heapify(heap)
            res = []
            for i in range(k):
                res.append(heapq.heappop(heap)[1])
            return res


        # return sorting_based(nums, k)
        return heap_based(nums, k)