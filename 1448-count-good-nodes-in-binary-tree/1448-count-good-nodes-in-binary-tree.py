# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        count = 0
        tmp = root.val

        def dfs(cur, max_val):
            nonlocal count
            if not cur:
                return 0
            if cur.val >= max_val:
                count += 1
                max_val = cur.val

            dfs(cur.left, max_val)
            dfs(cur.right, max_val)

        dfs(root, tmp)
        return count

        


'''
Good nodes : nodes less than the root node + path from root has no nodes > x

constraints : 
    - 1 -> 100 nodes
    - node.vals can be -100 -> 100

approach:
    we can perform DFS on it

    DFS :
        - keep running max of the node its currently at
        - if the nodes lower than the root val,
            -   dfs and pass in root, tmp val



'''
