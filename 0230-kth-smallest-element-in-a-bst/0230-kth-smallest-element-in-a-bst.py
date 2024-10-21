# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        res = 9999
        kth = 0
        
        def in_order(node):
            nonlocal kth, res
            if not node: return

            if node.left:
                in_order(node.left)
            kth += 1
            if kth == k:    
                res = node.val
                return 
            
            print(node.val)
            if node.right:
                in_order(node.right)
                
        in_order(root)
        return res
#         