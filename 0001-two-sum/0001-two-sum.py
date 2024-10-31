class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            t = target - nums[i]
            if t in hmap:
                return [hmap[t], i]
            else:
                hmap[nums[i]] = i

            # if nums[i] not in hmap:
            #     hmap[num[i]] = i
            
            
        
        
'''
Sum is 2 numbers that add up to product
target - n


'''