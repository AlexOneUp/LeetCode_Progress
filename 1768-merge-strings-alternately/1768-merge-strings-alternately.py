class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        
        w1 = 0
        w2 = 0
        while w1 != len(word1) or w2 != len(word2):
            
            if w1 != len(word1):
                merged += word1[w1]
                w1 += 1
            if w2 != len(word2):    
                merged += word2[w2]
                w2+=1
        return merged