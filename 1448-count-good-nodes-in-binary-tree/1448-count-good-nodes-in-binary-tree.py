# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        
        def dfs(cur, max_val):
            nonlocal count
            if not cur:
                return 0
            if cur.val >= max_val:
                count += 1
                max_val = cur.val
            dfs(cur.left, max_val)
            dfs(cur.right, max_val)
        
        dfs(root,root.val)
        return count
        
# Approach
# DFS from left to right returning all nodes that are greater or equal to the root node