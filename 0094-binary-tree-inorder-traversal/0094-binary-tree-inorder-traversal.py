# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        def traverse(curr):
            if curr.left != None:
                traverse(curr.left)
            res.append(curr.val)
            if curr.right != None:
                traverse(curr.right)
        if root != None:
            traverse(root)
        return res