class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for file in logs:
            if file != '../' and file != './':
                res += 1
            if file == '../' and res != 0:
                res -= 1
            else :
                continue

        return res