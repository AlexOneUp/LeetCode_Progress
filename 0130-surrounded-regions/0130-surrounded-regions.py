class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        # Change unsurrounding regions
        def dfs(i, j):
            if i < 0 or j < 0 or i == ROWS or j == COLS or board[i][j] != "O":
                return
            # Changes to T instead of O or X
            board[i][j] = "T"
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # Step 1
        # change the border elements to something else
        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS - 1] == "O":
                dfs(row, COLS-1)
                
        for col in range(COLS):
            if board[0][col] == "O":            
                dfs(0, col)
            if board[ROWS - 1][col] == "O":
                dfs(ROWS - 1, col)


        ## Step 2
        # Change the remaining inside regions from O -> X
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O": board[row][col] = "X"
        
        #STEP 3 
        # Change back the border elements to regions
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T": board[row][col] = "O"      


'''
Input: board = [
  ["X","X","X","X"],
        _______
  ["X",|"O","O"|,"X"],
  ["X",|"O","O"|,"X"],
       |_______|
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]


Intuition: 
    - surrounded = 0's surrounded by X / while NOT on Borders
        - regions ON the border aren't changed / visited
        - i...ROWS
        
    - what if nodes inside are connected to borders?
        change nodes within border
    - dfs on nodes

'''