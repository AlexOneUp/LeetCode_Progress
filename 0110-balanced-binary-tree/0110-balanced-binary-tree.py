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
        
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)    
            
            if abs(left - right) > 1: 
                res = False
            return max(left, right) + 1
        
        dfs(root) 
        
        return res
        
        

            
# A binary tree is considered to be balanced when the difference in height of left and rightof node/root exist in the range <=1.