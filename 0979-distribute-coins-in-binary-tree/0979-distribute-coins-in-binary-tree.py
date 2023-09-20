# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num_moves = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def give_coins(node):
            nonlocal res
            if not node: return 0
            left = give_coins(node.left)
            right = give_coins(node.right)
            res += abs(left) + abs(right)
            return node.val + left + right - 1
        give_coins(root)
        return res
# 
# 
# 
# 
# 
# 
# 
# 
# 
        
        