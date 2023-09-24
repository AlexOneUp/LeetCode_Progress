# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        def dfs(node):
            print(res)
            if not node:
                return
            res.append(node.val)
            return dfs(node.left) or dfs(node.right)
        dfs(root)
        return res