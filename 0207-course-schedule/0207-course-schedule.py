class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {edge: [] for edge in range(numCourses)}
        
        for u, v in prerequisites:
            adj_list[u].append(v)
        visited = set()
            
        def dfs(course):
            if course in visited: return False # cycle found
            
            if adj_list[course] == []: return True #init path
            
            visited.add(course) #visiting current path
            
            for pre_req in adj_list[course]: # fo
                if not dfs(pre_req): return False
            
            visited.remove(course)
            adj_list[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True