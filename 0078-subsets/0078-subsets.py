class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        sub = []
        
        # The input is actually the index of nums
        def dfs(idx):
            # For size of nums append a subset copy until the end
            if idx >= len(nums):
                res.append(sub.copy())
                return
            
            # Decision to add element
            sub.append(nums[idx])
            dfs(idx + 1)
            
            # Don't add the element
            sub.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res