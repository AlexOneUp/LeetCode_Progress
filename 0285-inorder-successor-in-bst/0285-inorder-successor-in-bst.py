# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        found_p = False
        
        def dfs(node):
            nonlocal successor, found_p
            if not node: return
            
            dfs(node.left)
            if found_p and successor is None:
                successor = node
                return
            
            if node == p:
                found_p = True
            
            dfs(node.right)
        dfs(root)  
        return successor
        
        
        
'''
Return in-order successor node in BST

If not success, return None


successor node def: node p is node smallest key > p.val


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


root = [5,3,6,2,4,null,null,1], p = 4

intuition :
    The in-order successor is the parent of p :
        if p.val < parent.val
            if the parent is less then p, then we just return
        else if parent.val > p.val, return the parent val
    - we can do dfs on the tree w/ in-order traversal :
        we want to stop at p if we reached p.val
        then look at the parents.
        
    
 '''