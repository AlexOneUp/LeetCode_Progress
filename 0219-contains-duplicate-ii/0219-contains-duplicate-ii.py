class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}    
        l = 0
        r = 1
        for idx in range(len(nums)):
            if nums[idx] in hashmap and abs(idx - hashmap[nums[idx]]) <= k:
                return True
            hashmap[nums[idx]] = idx
        return False