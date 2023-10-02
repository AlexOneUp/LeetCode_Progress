class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        if digits == "":
            return []
        res = []
        # digits.split()
        digits = list(digits)
        
 
        def dfs(idx, substr):
            if len(substr) == len(digits):
                res.append(substr)
                return
            for c in hmap[digits[idx]]: 
                dfs(idx + 1, substr + c)   
                
        if len(digits) > 0:
            dfs(0, "")
        
        return res
            
            