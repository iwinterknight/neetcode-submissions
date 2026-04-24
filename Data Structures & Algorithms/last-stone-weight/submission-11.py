class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        for stone in stones:
            heapq.heappush(self.heap, -stone)
        
        while len(self.heap) > 1:
            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)
            if abs(x-y) > 0:
                heapq.heappush(self.heap, -abs(x-y))
        
        return -self.heap[0] if self.heap else 0