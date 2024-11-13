class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {node: [] for node in range(numCourses)}  # Initialize each node with an empty list

        for node in prerequisites:
            course, prerequisite = node
            adj_list[course].append(prerequisite) 

        visited = set()
        
        def dfs(course):
 
            if course in visited:
                return False
            
            #If the course adj_list is empty
            # Then, we know that course can be completed
            if adj_list[course] == []:
                return True
            visited.add(course)
            
            for pre_req in adj_list[course]:
                # If the course cannot be completed 
                # If the course has been visited before
                if not dfs(pre_req): return False
            
            # Remove from visted set if a course can be completed
            visited.remove(course)
            adj_list[course] = []
            
            return True
        
        
        for course in range(numCourses):
                if not dfs(course): return False
        return True
        
        
'''
is it possible to finish all courses

0 - > [1]

build out adjacency list
hashmap
basecase:
    when a node does not have a pre-requisite


'''