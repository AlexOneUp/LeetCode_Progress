# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):

            
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)    
            
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]     
        return dfs(root)[0]
        

            
# A binary tree is considered to be balanced when the difference in height of left and rightof node/root exist in the range <=1.