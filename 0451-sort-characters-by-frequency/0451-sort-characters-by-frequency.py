class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        
        letters = dict.fromkeys(string.ascii_letters+string.digits, 0)
        
        for letter in s:
            letters[letter] += 1
        letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
        letters = dict(letters)
        
        for k,v in letters.items():
            if v > 0:
                res += k * v  
            continue

        return res