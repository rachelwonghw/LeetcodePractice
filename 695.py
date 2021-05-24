class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(grid, i - 1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1) \
                + dfs(grid, i, j + 1)

        
        if not grid or len(grid) == 0:
            return 0
        
        max_area_of_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area_of_island = max(dfs(grid, i , j), max_area_of_island)
                    
        return max_area_of_island