# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        res = TreeNode(root)
        def dfs(node):
            if not node:
                return
            
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
                
            if node.val == target and not node.left and not node.right:
                return None

            
            return node
        
        return dfs(root)
            
            