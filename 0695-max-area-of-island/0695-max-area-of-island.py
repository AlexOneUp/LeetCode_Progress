class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        row, col = len(grid), len(grid[0])

        # basic dfs island traversal
        # if island is found
        def dfs(i, j):
            nonlocal row, col
            
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0
            
            #visited land piece
            grid[i][j] = 0
            area = 1
            
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            
            return area
            
            
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    prevIsland = dfs(i, j)
                    maxIsland = max(maxIsland, prevIsland)

        
        return maxIsland