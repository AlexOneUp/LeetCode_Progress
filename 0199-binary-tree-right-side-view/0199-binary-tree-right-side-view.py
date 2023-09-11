# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        q = deque([root])
        while q:
            right = None
            len_q = len(q)
            # Pops every node in current level
            # Takes children and adds them into the queue
            for i in range(len_q):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:      
                res.append(right.val)
        
        return res
                    