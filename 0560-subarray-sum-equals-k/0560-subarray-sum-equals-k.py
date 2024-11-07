class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        hmap = {0 : 1} # handling subarrays starting from 0th element
        
        for num in nums:
            
            prefix_sum += num
            
            if prefix_sum - k in hmap:
                res += hmap[prefix_sum - k]
            
            if prefix_sum in hmap:
                hmap[prefix_sum] += 1
            else:
                hmap[prefix_sum] = 1

        return res