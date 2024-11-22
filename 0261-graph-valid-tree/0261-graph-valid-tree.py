class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build the adjacency list
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()  # To track visited nodes

        # DFS function to detect cycles and check connectivity
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, node):  # Recursively visit neighbors
                        return False
                elif neighbor != parent:  # Cycle detected
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):  # -1 is used as the parent of the root node
            return False

        # Ensure all nodes are visited (graph is connected)
        return len(visited) == n



'''
UMPIRE



_____________________
U:
    - undirected eges
    - valid tree?
        - theres 1 root node
            + nodes MUST have 1 parent
            + parents can have k children
        - **non acyclic graph**
        - graph where 2 nodes are connected by exactly 1 path
        
    Example :
    
    valid tree
        0
     / / \ \
    1  2 3  4
    |      /
    5     6
   /
  7
    
    
    valid tree
     0      1
      \      \
      2       3  
      
      invalid tree
      0     1
       \   / 
         2
        
    invalid tree
        0
     / / \ \
    1  2 3  4
    |     \ /
    5      6
   /
  7

_____________________
M:
    - recursive approach
        + dfs topological sort 
            ++ **cycle detection**
            ++ O(V + E)
_____________________
P:
    - adj list :
        + parent : child
    - parent_node
    - NODES STATES :
        + visited : hashmap
            ++ children : 1 parent (parent node)
                +++ if child has a parent already, cycles detected 
                    ++ return false
                +++ otherwise put into visited hashmap with the parent
    - dfs(child_node):
            + nonlocal parent_node
            + if node == visited[node]:    if the parent is seen in the hashmap
                ++ return False
            + otherwise :
                ++ put the node into visited[node] = parent_node
            
            + for node in adj_list[node]:
                ++ parent_node = node
                ++ if not dfs(node): return False
        
    - return True


_____________________

I:

'''