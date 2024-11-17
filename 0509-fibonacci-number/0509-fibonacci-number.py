class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        
        dp = [0] * (n + 1)
        
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
        
'''

Intuition:
    Using Bottom-Up Tab approach:
        Iterative solution
        
        An iterative approach 
            - solve all subproblems first
                + use their results to build up to the solution of the main problem.
        
'''