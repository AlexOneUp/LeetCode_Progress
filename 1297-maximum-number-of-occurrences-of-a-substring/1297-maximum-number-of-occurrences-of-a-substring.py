'''
# of unique chars in substr -> chars <= maxLetters

Naive approach O(n^2)
'''
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        str_occurs = dict()
        
        # sliding window to check for all possible types of permutations
        idx = 0
        
        max_occ = 0
        while idx <= len(s) - minSize:

            substr = s[idx:idx + minSize]
            uni_ch = set(substr)
            
            # for ch in substr:
            #     # Unique character and the size of unique characters does not exceed maxLetter
            #     if ch not in uni_ch:
            #         uni_ch.add(ch)
            
            if len(uni_ch) <= maxLetters:
                if substr in str_occurs:
                    str_occurs[substr] += 1
                else:
                    str_occurs[substr] = 1           
                max_occ = max(max_occ, str_occurs[substr])
            
            idx += 1
        return max_occ
                    