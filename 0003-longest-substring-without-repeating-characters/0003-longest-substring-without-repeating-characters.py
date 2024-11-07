class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        substr = set()
        left, right = 0, 0
        
        for right in range(len(s)):
            # sliding window 
            if s[right] in substr:
                # finds the length of running substring
                while s[right] in substr:
                    substr.remove(s[left]) 
                    left+=1
                substr.add(s[right])
                # starts a new substr
                
                    
            else:
                substr.add(s[right])
                res = max(res, right - left + 1)

                
        return res
        
        
'''
Find LENGTH longest substring (unique chars)

Intuition :
    - each substring is unique chars
        -storage / lookup on these chars?
            - set
    - iter through s
        keep track of the longest substring if theyre unique characters
            - we know characters unique if its in our set
                O(1) look up
    - if is unique add to set
    - if not, we move onto next character
        pop chars from substr by Longest substr times
    
    - sliding window appraoch

'''