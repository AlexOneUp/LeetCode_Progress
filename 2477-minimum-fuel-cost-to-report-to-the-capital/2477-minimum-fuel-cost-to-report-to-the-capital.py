class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = defaultdict(list)
        for src, des in roads:
            adj_list[src].append(des)
            adj_list[des].append(src)
        
        res = 0 
        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in adj_list[node]:
                if child != parent:
                    p = dfs(child, node)
                    passengers += p
                    res += int(ceil(p / seats))      
            return passengers + 1 
        
        dfs(0,-1)
        return res
    
#     This code calculates the minimum fuel cost required to reach the capital city from all other cities. The code follows the following steps:

# Creation of adjacency list: The input roads list is converted into an adjacency list representation, where each city is a key and its corresponding neighbors are stored in a list. The dictionary adjacency_list is used for this purpose.
# Initializing the fuel cost: A list total_fuel_cost is created with a single element to store the minimum fuel cost, initialized to 0.
# Defining the DFS function: A recursive DFS function dfs is defined, which takes two arguments: the current node being processed and its parent node.
# Keeping track of the people: In each call of the DFS function, a variable people is used to keep track of the total number of people in the subtree rooted at the current node. Initially, the number of people is set to 1 to account for the person at the current node.
# Processing the neighbors: For each neighbor of the current node, the DFS function is called, and the number of people in the subtree rooted at the neighbor is added to the variable people. If the neighbor is the same as the parent, the loop continues to the next neighbor to avoid visiting the same node twice.
# Adding the fuel cost: If the current node is not the capital city (node 0), then the fuel cost to reach the capital city from this node is calculated. The formula used to calculate the fuel cost is math.ceil(people / seats). This cost is then added to the total fuel cost stored in total_fuel_cost[0].
# Returning the people: Finally, the function returns the number of people in the subtree rooted at the current node.
# Calling the DFS function: The DFS function is called with node 0 and None as the parent, which signifies that node 0 is the root of the tree and has no parent.
# Returning the result: The final result, which is the minimum fuel cost, is returned by the main function.