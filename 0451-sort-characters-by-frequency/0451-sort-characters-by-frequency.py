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
            else:
                break

        return res
    
    """
    Approach :
        HashMap of all ASCII characters + digits with default value = 0
        +1 to the key for every time it appears in the string
        
        Main idea is the sorted() function to sort the hash map. and reverse the sort so the most frequent are up top
        then just remake it from a list back into a dictionary
        
        Python specific k, v loop through now sorted hashmap
            if the value is > 0 
                append k, v times to res
            break the loop if this isn't true anymore.
        return res
    """