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
        if not root and subRoot:
            return False
        
        
        if self.compare_tree(root, subRoot) == True:
            return True

        if self.isSubtree(root.left, subRoot) == True:
            return True
        elif self.isSubtree(root.right, subRoot) == True:
            return True
        else:
            return False


    def compare_tree(self, cur, sub_cur):
        if not cur and not sub_cur:
            return True

        if (cur and sub_cur) and (cur.val == sub_cur.val):
            return (self.compare_tree(cur.left, sub_cur.left) and self.compare_tree(cur.right, sub_cur.right))
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