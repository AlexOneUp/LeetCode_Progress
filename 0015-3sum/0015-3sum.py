class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()
        res = []
        print(nums)
        
        for i in range(len(nums)):
            # Take care of the duplicate scenario
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # next values of a 
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                # a + b + c = 0
                three = nums[i] + nums[l] + nums[r]
                if three < 0: l += 1
                elif three > 0: r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res
                    

'''
We want a list of lists of all triplet numbers that sum to 0 

Questions:
    - Is the array sorted? 
        no
    - min length?
        3
    - can result contain dupes?
        no

Intuition:
    - Want distinct triplet numbers that sum to 0
    - Sorting the array makes it easier
    
Approach :
    1. sort array
    2. we can break it down as a + b + c
        tackle this incrementally
        a is the first iteration of each + finds duplicates
        b and c can be tackled with 2 ptr
    


'''