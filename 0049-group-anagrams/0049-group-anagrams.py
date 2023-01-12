class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         hashmap = {}

#         for subStr in strs:
#             sortWord = ''.join(sorted(subStr))

#             if sortWord not in hashmap:
#                 hashmap[sortWord] = [subStr]
#             else:
#                 hashmap[sortWord] += [subStr]
#         return list(hashmap.values())

# Create an empty dictionary to store the anagrams
        anagrams = {}
        # Iterate through the list of strings
        for s in strs:
            # Count the number of each character in the string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Use the count as a key to store the original string in the dictionary
            count = tuple(count)
            if count in anagrams:
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]
        # Return the values of the dictionary
        return list(anagrams.values())