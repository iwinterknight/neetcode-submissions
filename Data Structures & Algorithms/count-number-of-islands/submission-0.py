class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, visited):
            visited.add((r, c))
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)

        num_islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    num_islands += 1

        return num_islands