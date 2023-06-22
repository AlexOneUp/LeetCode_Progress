class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = dict()
        
        for n in arr:
            if n not in hmap:
                hmap[n] = 1
            else :
                hmap[n] += 1   
#         Pointer to last value

        hmap2 = dict()
        for k, v in hmap.items():
            if v in hmap2:
                return False
            else:
                hmap2[v] = 1
        return True
        # print(hmap)
       