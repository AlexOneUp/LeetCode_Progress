class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)
'''
MEMOIZATION :
{

}

                    F(6) decision tree
            F(5)           F(4)
        F(4)  F(3)       F(3) F(2)
      F(3) F(2) 
Intuition :
    - Top-down memoization approach
    
    


'''