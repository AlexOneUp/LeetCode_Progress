# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:    
            return root
    
    
        
        
'''
Recursive approach :


given p, q values

find LCA of the nodes that are between p and q

scenarios :
    1. if p, q > root, go right
    2. if p, q < root, go left

    3. if p > root, q < root, then the root must be the LCA
    OR
    4. if p < root, q > root, then root also must be the LCA
    OR
    5. if p or q is == root, then the LCA must be itself (root)


ex: 
scenario 3: 
    p, q = 0, 4
    res = 2

Time : O(logn) for every half of the subtree
Space : O(1)

'''