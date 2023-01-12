class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for subStr in strs:
            sortWord = ''.join(sorted(subStr))

            if sortWord not in hashmap:
                hashmap[sortWord] = [subStr]
            else:
                hashmap[sortWord] += [subStr]
        return list(hashmap.values())
