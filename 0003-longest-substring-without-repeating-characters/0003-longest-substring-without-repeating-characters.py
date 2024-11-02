class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        charSet = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                # Slides window by removing from the set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            # Compute the maxmimum substring because the substring is length of right - left pointer
            res = max(res, r - l + 1)
        return res
        
'''
Intuition :
    - Find longest substr wihtout repeating chars
    - 

'''