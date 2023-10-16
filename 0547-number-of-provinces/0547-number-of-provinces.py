class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        total_provinces = 0
        
        
        cities_in_row = len(isConnected)
        # Represents the columns
       
        visited = { 
            city : False for city in range(cities_in_row) 
        }  #{ 0: False, 1: False, 2: False }
    
        # Iter through the rows and see if there is a connecting city.
        def dfs(row):
            for col in range(cities_in_row):
                if isConnected[row][col] and not visited[col]:
                    visited[col] = True
                    dfs(col)
        
        # For the cities in a current row, if they weren't visited, do DFS on the   
        for city in range(cities_in_row):
            if not visited[city]:
                dfs(city)
                total_provinces += 1
        return total_provinces
        
#         def mark_province_visited(graph, starting_city, visited):
#             stack = []
#             stack.append(starting_city)
            
#             while len(stack) > 0:
#                 starting_city = stack.pop()
                
#                 neighbors = graph[starting_city]
                
#         for city in range(cities_in_row):
#             if city in visited: continue
            
#             total_provinces += 1
#             mark_province_visited(isConnected, city, visited)
            

#         # Rows
#         for i in range(rows):
#             # Cols
#             for j in range(cols):
#                 if isConnected[i][j] == 1:
#                     dfs(isConnected, i, j)
#                     num_pr += 1

#         return num_pr
        
        
        
# Initial Approach
# Info ;
# PROVINCES CAN BE BOTH Connected OR Unconnected
# As you traverse the graph, flag the visited provinces.

# [        0 1 2 -> visited Set
#       _________
#     0 | [1,1,0],  
#     1 | [1,1,0], [0]->[1]
#     2 | [0,0,1]   [2]
#       Num Provinces = 2
# ]

# [
#     [1,0,0],
#     [0,1,0],
#     [0,0,1]
# ]