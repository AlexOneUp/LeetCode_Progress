class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        subset = []
        
        def dfs(idx):
            # If we've reached the end, just copy last value
            if idx >= len(nums):
                res.append(subset[::])
                return
            
            #Decision to add the tree path
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()
            
            # Since nums is now sorted, we will look at the neighbor and see if it's the same value as the current index
            # If it is, keep iterating over the duplicate value.
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                # Iterate over the current idx because it's the same value.
                idx += 1
                
            # Case that adds empty array at the end
            dfs(idx + 1)
            
        dfs(0)
        return res[::-1]
            