class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def backtrack(path):
            if len(path) == len(nums):
                #append copy of the path
                perms.append(path[:])
                return
            
            for num in nums:
                if num in path: continue
                
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return perms
        
'''
Generating permuatations

uses path list to store current permutations
tracks 'used' #s to avoid dupes



'''