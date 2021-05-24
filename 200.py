from collections import deque
# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):
            if  i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
                return 0
            
            grid[i][j] = '0'
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            return 1
        
        
        if not grid or len(grid) == 0:
            return 0
        
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == '1':
                    num_of_islands += dfs(grid, i, j)
                
        
        return num_of_islands

#bfs
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0:
            return 0
        
        stack = deque()
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == '1':
                    num_of_islands += 1
                    stack.append((i,j))
                    grid[i][j] = '0'
                    while stack:
                        m, n = stack.popleft()
                        if m - 1 >= 0 and grid[m-1][n] == '1':
                            stack.append((m-1,n))
                            grid[m-1][n] = '0'

                        if n - 1 >= 0 and grid[m][n-1] == '1':
                            stack.append((m,n-1))
                            grid[m][n-1] = '0'

                        if m + 1 < len(grid) and grid[m+1][n] == '1':
                            stack.append((m+1,n))
                            grid[m+1][n] = '0'

                        if n + 1 < len(grid[m]) and grid[m][n+1] == '1':
                            stack.append((m, n+1))
                            grid[m][n+1] = '0'
                
                
        
        return num_of_islands