# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sums = []
        # Bottom up approach
        def dfs(node):
            if not node: return 0
            
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            
            cur_sum = sum_left + sum_right + node.val
            
            tree_sums.append(cur_sum)
            # Total sum of the tree to do the computation
            return cur_sum
        
        total_sum = dfs(root)
        
        max_product = 0
        
        for each_sum in tree_sums:
            max_product = max(max_product, each_sum * (total_sum - each_sum))
        return max_product % (10**9 + 7)