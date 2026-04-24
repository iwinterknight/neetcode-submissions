class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        if not q and not fresh:
            return 0

        minutes = 0
        while q:
            for _ in range(len(q)):
                r, c  = q.popleft()
                
                for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= i < R and 0 <= j < C and grid[i][j] == 1 and (i, j) not in visit:
                        q.append((i, j))
                        visit.add((i, j))
                        fresh -= 1

            minutes += 1

        if fresh:
            return -1
        return minutes - 1