class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = min(grid[r][c], dist)
                visited.add((r, c))

                for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] != -1 and (i, j) not in visited:
                        queue.append((i, j))
            dist += 1