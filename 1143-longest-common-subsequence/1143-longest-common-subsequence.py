class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Creating the matrix / 2D array of nodes in the decision trees (2D - DP)
        matrix = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        # Bottom up traversal of matrix
        for i in range(len(text1) - 1, -1, -1):
        #     
            for j in range(len(text2) -1, -1, -1):
            # If the text in the same position match, then traverse diagonally and iter
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
            # Otherwise if the characters don't match, Find the maximum of the values 
            # Both to the right, and up of our current node
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])
        print(matrix[0][0])
        
        return matrix[0][0]
    
    # T: O(N*M) for first string and 2nd string creating a matrix
    # S: O(N*M) for the matrix