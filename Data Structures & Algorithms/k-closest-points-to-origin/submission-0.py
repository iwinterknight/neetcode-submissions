class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def solve(points, k):
            heap = []
            for point in points:
                d = pow(point[0], 2) + pow(point[1], 2)
                heapq.heappush(heap, (-d, point))
                if len(heap) > k:
                    heapq.heappop(heap)
            res = [point for _, point in heap]
            return res

        return solve(points, k) 
