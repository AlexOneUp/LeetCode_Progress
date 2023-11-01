class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = { '../' : -1, './': 0 }
        
        res = 0
        
        for log in logs:
            if log not in ops:
                res += 1
            if log in ops and res != 0:
                res += ops[log]

        return res