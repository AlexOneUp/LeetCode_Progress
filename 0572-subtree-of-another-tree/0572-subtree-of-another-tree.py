# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # This way you know both trees are not empty.
        # order matters
        if not subRoot: 
            return True
        if not root:
            return False
        
        if self.same(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        
        
    # Compares trees to see if they're the same    
    def same(self, root, subRoot):
        # NULL trees are the same
        if not root and not subRoot:
            return True
        # Look at leaf nodes and recursively look at the subtrees
        if root and subRoot and root.val == subRoot.val:
            return (self.same(root.left, subRoot.left) and
            self.same(root.right, subRoot.right))
        # If there are any extra nodes, then they cannot be subtrees of eachother
        return False

# Edgecases:
#   if both trees are null, theyre same
#   
# 
# 
# 
# 
# 
# 