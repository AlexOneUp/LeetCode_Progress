class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        subsets = []
        unique = []
        def backtrack(start, path):
            if len(path) == k: 
                #append copy of path
                subsets.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(1, [])
        return subsets
                
'''
n up to 20
1 <= k <= n


'''