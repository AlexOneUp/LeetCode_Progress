class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        for num in nums:

            hashmap[num] = hashmap.get(num,0) + 1        

            if hashmap[num] > 1:
                return True
        return False    
                