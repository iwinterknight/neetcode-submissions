class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def solution_1():
            counts = defaultdict(int)
            for num in nums:
                counts[num] += 1
            counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
            res = []
            for i in range(k):
                res.append(counts[i][0])
            return res

        def solution_2():
            import heapq
            min_heap = []
            counts = defaultdict(int)
            for num in nums:
                counts[num] += 1

            for num, freq in counts.items():
                heapq.heappush(min_heap, (freq, num))
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
            
            return [num[1] for num in min_heap]

        return solution_2()

