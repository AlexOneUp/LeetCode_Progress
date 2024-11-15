class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_count = {}
        left = maxWindow = 0
        for right in range(len(s)):
            # if the characters in the dict, otherwise init with 0
            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                
                left += 1
                
            maxWindow = max(maxWindow, right - left + 1)
            
        return maxWindow
''' 
UMPIRE method:
    
UNDERSTAND :
    return longest substring S with at most K distinct chars
        - 'eceba', k = 2
          + 'ece' length 3
        - 'ekbbeuec' k = 2
          + 'beuec' length 5
     
MATCH :
    - sliding window + hashmap 
        + hashmap keeps count k unique characters
            {
            'b':1
            'e':2
            'u':1
            'c':1
            }
        + sliding window keeps tracking of current length of substring

PLAN :
    - 2 ptrs
        - move right pointer to increase window size
            - until the window is MORE than K unique counts in hashmap
                - slide the start of window
            - take the max of the current window 
IMPLEMENT :
    - init : 
        char_counts - dict()
        - 2 ptr
            left = 0
            maxWindow = 0
    - for right in range(len(string)):
        + charcounts[char] = 1 + char_counts.get(string[right], 0)
        while (right - left + 1) - count
        maxWindow = max(maxWindow, right - left + 1)
    
    
REVIEW :
EVAL :




'''