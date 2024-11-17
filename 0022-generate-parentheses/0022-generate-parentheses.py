class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(curr, opening, closing):
            
            if opening == n and closing == n: # if theres an opening and closing bracket, then we know its a well-formed parenths
                res.append(curr)
                return
            
            if opening < n: backtrack(curr + '(', opening + 1, closing)
            
            if closing < opening: backtrack(curr + ')', opening, closing + 1)
            
        backtrack('', 0 , 0)
        return res
            
'''

Intuition:
    - there has to be opening and closing brackets
    - 1. we never add more opening/closing N brackets
    - 2. # closing parentheses never exceeds opening brackets

UMPIRE:

U :
    - generate all combos of "well-formed" parenths for N 
        "()" has opening with closing brackets
        
        
M :
    - DFS backtracking approach brute force
        - generates a 2^n # of subsets
        
P :
    - general backtrack approach
        + decision to add
        + recurse
        + base case
        + undo decision
    - Backtrack with start, subset:

        + add a copy of the current path to curr_subset
        
        + iterate through subset from start
            - DECISION TO ADD
            ++ append current path
            - RECURSE
            ++ backtrack    
            UNDO
            pop from path
        
        
'''