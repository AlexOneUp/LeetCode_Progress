class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'I':1, 
            'V':5, 
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        for ch in range(len(s)):
            if ch < len(s) - 1 and hmap[s[ch]] < hmap[s[ch+1]] :
                res -= hmap[s[ch]]
            else:
                res += hmap[s[ch]]
        return res
            
    
    
    # The key intuition lies in the fact that in Roman numerals, when a smaller value appears before a larger value, it represents subtraction, while when a smaller value appears after or equal to a larger value, it represents addition.