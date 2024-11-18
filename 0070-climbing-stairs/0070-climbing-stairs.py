class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {
            1:1, 
            2:2
        }
        
        def dp(i):
            if i in memo: return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        dp(n)
        return memo[n]
    
    
'''
N steps to reach top
    -Can climb 
        1 steps
        2 steps

UMPIRE

U :
    - There are repeated sub problems
        n = 2
        [1,1], [2] = variations
        
        n = 5
        [1,1,1,1,1],[1,1,1,2],[2,2,1],[1,2,2], ..., 
        

        
M :

    Either backtrack or DP to solve
        - dp top down - memo
P :
    1. Memoize the initial 2 steps for base case
        

'''