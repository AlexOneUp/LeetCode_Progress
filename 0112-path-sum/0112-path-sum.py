# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def bfs(node):
  
            if not node: return False

            q = deque([(node, node.val)])
            
            while q:
                
                cur, cur_sum = q.popleft()

                if not cur.left and not cur.right and cur_sum == targetSum:
                    return True

                if cur.left : 
                    q.append((cur.left, cur_sum + cur.left.val))
                    
                if cur.right : 
                    q.append((cur.right, cur_sum + cur.right.val))
            return False

        return bfs(root)

        
        
'''
root to leaf path

such that all values == targetSum

intuition:
    - dfs approach for a path
    - we want to try bfs approach




'''