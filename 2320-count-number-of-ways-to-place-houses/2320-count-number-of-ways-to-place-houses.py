class Solution:
    def countHousePlacements(self, n: int) -> int:
        memo = {0:1, 1:2}
        
        def dp(i):
            if i in memo: return memo[i]
            
            #top down
            memo[i] = dp(i-1) + dp(i - 2)
            return memo[i]
        
        total_ways = (dp(n)**2) % (10**9+7)
        
        return total_ways
'''
_______________________
Intuition
_______________________
    n*2 plots
        - n plots on a street
        - plots : 1 => n
            + house can be placed
    
    Requirement:
        - return # ways houses can be placed
            + no 2 houses are adjacent 
                + same street
        - return RESULT % (10^9 + 7)
        
    Note :
        - house on i plot / street
            + house can be placed on i plot / adjacent street


_______________________

UMPIRE
_______________________
U:
    plots have 2 sides
    each plot is a 4 part quadrant
    
    Restraints:
        - no 2 houses adjacent (next to each other on a street)
        - no need for house on a plot
    n = 1
    res = 4
        1.[]
        2.[1]
        3.[2]
        4.[1,2]
_______________________
M :
    - dp top-down approach with memo (brute force)
        + dp[i] : # of ways a house can be arranged on a plot[i]
    - start memo with :
        dp[0] = 1
        dp[1] = 2
    - There's plot ways to do dp[0],dp[1]
        + total ways = dp[n] * dp[n]
_______________________
_______________________
P :
    - calc 1 side of street of (dp[n])
        = dp[n]^2


'''