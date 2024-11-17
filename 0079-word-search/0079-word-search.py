class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        
        path = set()
        def dfs(r, c, char):
            if char == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[char] != board[r][c] or (r,c) in path: # if we see the same character, or we've visited a position before + OOB rules
                return False
            
            path.add((r, c)) # adds the coords if 
            
            res = (dfs(r+1, c, char+1) or dfs(r-1, c, char+1) or dfs(r, c+1, char+1) or dfs(r, c-1, char+1))
            
            # removes the current path from path because we traverse 1 extra time
            path.remove((r, c))
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
            
        return False
'''
UMPIRE
____________________________
Understand
____________________________
    - from board
    - construct if word exists
        + path
    - if not, return False

____________________________
____________________________
Match
    - dfs brute force to get path of words.
        - until we get to end of word
            - keep track of pointers that iterate if we found words
            - if we didn't find the words, travel back up 
        - Would need to backtrack in this case:
            


____________________________
____________________________
Plan




____________________________


'''