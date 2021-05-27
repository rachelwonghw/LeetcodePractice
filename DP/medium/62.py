class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        grid = [[1 for x in range(n)] for y in range(m)]

        for i in range(m):
            for j in range(n):
                # case for start
                if i - 1 >= 0 and j - 1 >= 0: 
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                # case
                else:
                    # do nothing
                    continue

        return grid[m-1][n-1]