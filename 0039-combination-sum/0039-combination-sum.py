class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        unique = []
        def dfs(idx, total):
            if total == target:
                res.append(unique.copy())
                return
            if idx >= len(candidates) or total > target:
                return
                
            # Decision to add the candidate
            unique.append(candidates[idx])
            dfs(idx, total + candidates[idx])
            unique.pop()
            dfs(idx + 1, total)
        dfs(0, 0)
        
        return res