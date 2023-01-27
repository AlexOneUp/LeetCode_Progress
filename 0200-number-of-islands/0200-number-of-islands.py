class Solution {
    public int numIslands(char[][] grid) {
        
        //Set of boundaries in the matrix
        int rowEnd = grid.length - 1;
        int colEnd = grid[0].length - 1;
        
        int numberIslands = 0;
        //This 
        for( int i = 0; i < grid.length; i++ ) {
            for(int j = 0; j < grid[0].length; j++){ 
                if( grid[i][j] == '1' ) {
                    isIsland(grid, i, j, rowEnd, colEnd);
                    numberIslands++;
                }
            }
            
        }
        return numberIslands;
    }
    
    public void isIsland( char[][] grid, int i, int j, int rowEnd, int colEnd ) {
        //Boundary check 
        if( i >= 0 && i <= rowEnd && j >= 0 && j <= colEnd) { 
            if( grid[i][j] == '1' ) {
            
                grid[i][j] = '2';
                //DFS on piece of land
                isIsland( grid, i+1 , j , rowEnd, colEnd);
                isIsland( grid, i-1 , j , rowEnd, colEnd);
                isIsland( grid, i , j+1 , rowEnd, colEnd);
                isIsland( grid, i , j-1 , rowEnd, colEnd);
            }
        }   
    }
}

/**
Recursive DFS Approach :
____________________________
- Look through matrix and for each element, when we find land do DFS.
- Do a recursive DFS approach helper method to check whether or not there is an island with connected 1s
    + Do the recursion while in bound of the matrix.
- If it is an island, redefine the index at the V[i][j] (V =  vertex).


Time : O(m * n) for the matrix
Space : O(m * n) for the DFS CALL STACK
**/
