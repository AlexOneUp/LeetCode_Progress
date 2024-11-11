# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            # returns a count of value, node_sum
            if not node: return 0, 0
            
            # left and right subtree and the count of the nodes passed up
            left, left_node = dfs(node.left)
            right, right_node = dfs(node.right)
            
            # if the sum which is (sum of parent + left + right) // (count_nodes + 1)
            if (node.val + left + right) // (left_node + right_node + 1) == node.val:
                count += 1
            # left and right average and the left_nodes and right_nodes counters
            return node.val + left + right, left_node + right_node + 1
        dfs(root)
        return count
        