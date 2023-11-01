class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = { '../' : -1, './': 0 }
        
        res = 0
        
        for file in logs:
            if file not in ops:
                res += 1
            if file in ops and res != 0:
                res += ops[file]

        return res