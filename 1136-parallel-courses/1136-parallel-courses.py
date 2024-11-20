class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = {course: [] for course in range(1, n+1)}
        
        for u, v in relations:
            adj_list[u].append(v)
            
        cycle, visited = set(), {}
        
        
        def dfs(course):
            if course in visited: 
                return visited[course] # if we have seen the course before
            else: 
                visited[course] = -1 # cycle detection
            
            max_len = 1 # we are finding the longest path of the graph
            
            for end_node in adj_list[course]:
                length = dfs(end_node)
                if length == -1:
                    return 1
                else:
                    max_len = max(length + 1, max_len)    

            visited[course] = max_len
            return max_len
       
        max_len = -1
        
        for node in adj_list:
            length = dfs(node)
            if length == -1: # cycle detected we cant complete all courses
                return -1
            else:
                max_len = max(max_len, length)
                
        return max_len
        
'''
Intuition
    - n courses 
        - 1 -> n
    - relations [prev, next]
        - prev must be taken before next
    - if there are cycles, return -1
    

UMPIRE

U: 
    - must take ALL courses
    - return -1 if not able to (cycle found)
    
    Examples :
        [[1,3], [2,3]]
        res = 2 
        1: [3]
        2: [3]
        3: []
        
        [[1,3], [2,3],[3,1]]
        -1 detected a cycle
        
        [[1,2], [1,3], [2,3], [3, 4]]
        1 -> 2 -> 3 -> 4
        |
        3
        
    Course has 3 possible states :
    cycle - will also be visiting to reduce redundant logic
    visited
M: 
    - dfs topological sort
        - detect a cycle and know we cannot complete all courses
        - directed acyclic graph
        
P:
    - adjacency list : store prevCourses -> nextCourses
    - visting set
    - cycle set
    - semesters : int
    - dfs (top sort)
        + if a course found in cycle: return False
        + if a course found in visiting: return True
        + add course to the cycle if we passed the basecases
        + for element in adJ_list[course] :
            ++ recurse dfs
                ++ if its False, return False
        + remove course from cycle
        + add course to visited set
        + semesters + 1
        + return True to end the dfs
    - for course in range(n):
            -if a cycle was found 
        if not dfs(course): return -1
    - return semesters 
        
        
'''