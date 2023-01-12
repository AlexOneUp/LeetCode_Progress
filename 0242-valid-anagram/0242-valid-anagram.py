class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t) or len(set(s)) != len(set(t)) :
            return False
        for char in s:
            # 1 + hashmap.getOrDefault(key, defaultValue) Python equivalent
            hashmap[char] = hashmap.get(char, 0) + 1

 
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            else:
                return False
        # Check if there are any remaining contents in the hashmap. If there is, then it isn't an anagram
        
        # Check for each key, to see if it's values are now empty
        for val in hashmap.values():
            print(val)
            if val != 0:
                return False

        return True
