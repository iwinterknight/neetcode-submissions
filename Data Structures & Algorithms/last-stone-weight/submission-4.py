class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def solve(stones):
            heap = [-stone for stone in stones]
            heapq.heapify(heap)
            while heap:
                if len(heap) == 1:
                    return -heap[0]
                stone_1 = -heapq.heappop(heap)
                stone_2 = -heapq.heappop(heap)
                if stone_1 > stone_2:
                    heapq.heappush(heap, -(stone_1 - stone_2))
            return 0


        return solve(stones)