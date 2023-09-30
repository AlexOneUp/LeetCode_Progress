class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res = []
        
        hmap = dict()
        
        longer_arr = max(len(nums1), len(nums2))
        if longer_arr < len(nums1):
            for num in nums2:
                hmap[num] = 0
            for num in nums1:
                if num in hmap.keys():  
                    hmap[num] += 1
        else:
            for num in nums1:
                hmap[num] = 0
            for num in nums2:
                if num in hmap.keys():
                    hmap[num]+=1

        for k, v in hmap.items():
            if v > 0:
                res.append(k)
            
        return res