class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def solution_1(nums, k):
            counts = Counter(nums)
            counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            return [i for i, _ in counts][:k]

        def solution_2(nums, k):
            import heapq
            heap = []
            counts = Counter(nums)
            for num, count in counts.items():
                heapq.heappush(heap, (-count, num))
            res = []
            for i in range(k):
                res.append(heapq.heappop(heap)[1])
            return res

        def solution_3(nums, k):
            heap = []
            counts = Counter(nums)
            for num, count in counts.items():
                heapq.heappush(heap, (count, num))
                if len(heap) > k:
                    heapq.heappop(heap)
            res = []
            for i in range(k):
                res.append(heapq.heappop(heap)[1])
            return res[::-1]

        # return solution_2(nums, k)
        return solution_3(nums, k)