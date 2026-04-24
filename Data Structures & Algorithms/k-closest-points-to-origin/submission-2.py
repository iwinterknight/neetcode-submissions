class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2
        
        self.heap = []
        for point in points:
            print(distance(point), point)
            heapq.heappush(self.heap, (-distance(point), point))
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        return [point for _, point in self.heap]