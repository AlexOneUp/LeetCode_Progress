# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            level_avg, level_traversal = 0, len(queue)
            
            for _ in range(level_traversal):
                node = queue.popleft()
                level_avg = level_avg + float(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level_avg / level_traversal)
        print(res)
        return res