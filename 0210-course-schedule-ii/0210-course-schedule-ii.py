class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {node: [] for node in range(numCourses) }
        
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        res = []
        visited, cycle = set(), set()
        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            
            
            for pre in adj_list[course]:
                # if you detect a cycle
                if dfs(pre) == False: return False
                
                #if you haven't detected a cycle
            cycle.remove(course)
                
            visited.add(course)
            res.append(course)
            return True
        for c in range(numCourses):
                # if we detected a cycle, return empty list
            if dfs(c) == False:
                return []
            
        return res
'''
0 -> n-1 courses

must take B if u want to take A
[A, B]

return the order of courses to finish all courses

detect cycles
    - example [[1,0], [0,1]]
    
    
Topological sort



'''