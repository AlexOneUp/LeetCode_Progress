# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        res = []
        
        def bfs(node, height):
            nonlocal res
            if not node: return []
            
            q = deque([(node, height)])

            while q:
                cur, level = q.popleft()
                # a list for current level
                if level >= len(res): res.append([])
                    
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)
                
                if cur.left:
                    q.append((cur.left, level + 1))
                if cur.right:
                        q.append((cur.right, level + 1))
        bfs(root, 0)
        return res
        
        
        
'''

Intuition:
    Return level order traversal  zig zag @ every level
    
    starts - left right, alts to right-left
    heights - for every even level -> left - right
            - for every odd level -> right to left
    
    

[3,9,20,null,null,15,7, 14, 16, 5,8]

'''