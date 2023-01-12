class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
            if hashmap[num] >= 2:
               return True
            else:
                continue
        return False    
                