# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
 
        def dfs(left_st, right_st):
            # If there are no leaf nodes from root, then its balanced
            if not left_st and not right_st: return True
            # If there is no node on either side
            if not right_st or not left_st: return False
            
            # If the leaf node values are the same, call dfs
            if left_st.val == right_st.val:
                return dfs(left_st.right, right_st.left) and dfs(left_st.left,right_st.right)
            
        # def isMirror(t1, t2):
            # if not t1 and not t2:
            #     return True
            # if not t1 or not t2:
            #     return False
            # return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)        
            
        
        return dfs(root, root)