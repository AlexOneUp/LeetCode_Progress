class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {
            1: 1,
            2: 2
        }
        def backtrack(n):
            if n in memo:
                # Takes care of the base cases of when num is 1 or 2 because a HMap lookup is very efficient
                # Takes care of time excession
                return memo[n]
            
            memo[n] = backtrack(n - 1) + backtrack(n - 2)
            return memo[n]

        return backtrack(n)
