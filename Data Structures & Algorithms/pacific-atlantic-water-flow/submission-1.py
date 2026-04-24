class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])

        def scan(q):
            ocean = set()
            visit = set()
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    ocean.add((r, c))

                    for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= i < R and 0 <= j < C and heights[i][j] >= heights[r][c] and (i, j) not in visit:
                            q.append((i, j))
                            visit.add((i, j))
            return ocean

        q = deque()

        for i in range(R):
            q.append((i, 0))
        
        for j in range(1, C):
            q.append((0, j))

        pacific = scan(q)

        q = deque()

        for i in range(R):
            q.append((i, C-1))
        
        for j in range(C-1):
            q.append((R-1, j))

        atlantic = scan(q)

        return list(pacific & atlantic)




        