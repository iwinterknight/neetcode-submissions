class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visited, area=0):
            area += 1
            visited.add((r, c))
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j, visited, area)
            return area
        
        max_area = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j, visited)
                    max_area = max(max_area, area)
        
        return max_area