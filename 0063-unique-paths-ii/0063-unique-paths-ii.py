class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        # DP is the paths to the end/beginning
        # Memoize
        dp = [0] * n
        # Target to reach
        dp[n - 1] = 1
        
        # Traverse in reversed order 
        # T : O(n*m)
        # S : O(n)
        
        # Go through list of M rows in reverse order
        for row in reversed(range(m)):
            # Go through N columns in reverse order
            for col in reversed(range(n)):
                # If the row and col contains a valid path,
                # then make the dp @ this col = 0
                # otherwise, dp[col] is equal to value below it, which is dp[col] + dp[col + 1]
                if grid[row][col]:
                    dp[col] = 0
                # Out of bounds for col + 1 -> out of bounds
                elif col + 1 < n:    
                    dp[col] = dp[col] + dp[col + 1]
                # When value to the right is OOB
                # else:
                #     dp[col] = dp[col] + 0
        return dp[0]