class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {node: [] for node in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)

            
        cycle = set() #cycle detection
        visiting = set()
        unvisited = set()
        res = []
        def dfs(course):
            if course in cycle: # cycle found
                return False
            if course in visiting:
                return True

            cycle.add(course)
            
            for pre_req in adj_list[course]:
                if not dfs(pre_req):
                    return False
            cycle.remove(course)
            visiting.add(course)
            res.append(course)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return [] # detected a cycle, so we cannot finish courses
        return res
'''
UMPIRE:

U: 
    

'''