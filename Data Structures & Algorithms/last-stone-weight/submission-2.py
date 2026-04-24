class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        def solve(stones):
            heap = [-stone for stone in stones]
            heapq.heapify(heap)
            while len(heap) > 1:
                first = -heapq.heappop(heap)
                second = -heapq.heappop(heap)
                if first > second:
                    heapq.heappush(heap, second-first)
            return -heapq.heappop(heap) if len(heap) > 0 else 0


        return solve(stones)
