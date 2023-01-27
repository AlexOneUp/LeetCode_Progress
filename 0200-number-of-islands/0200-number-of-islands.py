class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowEnd = len(grid) - 1
        colEnd = len(grid[0]) - 1
        
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j,rowEnd,colEnd)
                    islands += 1
        return islands
    
    def dfs(self,grid, i, j, rowEnd, colEnd):
        if (i >= 0 and i <= rowEnd) and (j >= 0 and j <= colEnd):
            if grid[i][j] == '1':
                grid[i][j] = '2'
                
                self.dfs(grid, i+1, j, rowEnd, colEnd)
                self.dfs(grid, i-1, j, rowEnd, colEnd)
                self.dfs(grid, i, j+1, rowEnd, colEnd)
                self.dfs(grid, i, j-1, rowEnd, colEnd)