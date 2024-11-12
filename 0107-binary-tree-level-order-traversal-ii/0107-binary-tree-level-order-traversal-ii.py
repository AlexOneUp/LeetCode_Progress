# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = list()
        def bfs(node):
            nonlocal res
            if not node: return
            
            q = deque([node])

            while q:
                level = []
                size = len(q)
                
                
                for cur_node in range(size):
                    node = q.popleft()

                    level.append(node.val)
                    
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    
                res.append(level)    
                
        bfs(root)
        return res[::-1]
            
            
'''
post-order BFS approach

'''