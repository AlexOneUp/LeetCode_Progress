class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        #left side
        l_product = 1
        for i in range(len(nums)):
        
            res[i] *= l_product
            l_product *= nums[i]
            
        #right side
        r_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r_product
            r_product *= nums[i]
        return res
        
        
        
'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

1 -> 2*3*4 = 24
[1, 2, 3, 4]
<-^ ->

2 -> 1*3*4 = 12
[1, 2, 3, 4]
 <- ^ ->

3 -> 1*2*4 = 8
[1, 2, 3, 4]
    <- ^ ->


4 -> 1*2*3 = 6
[1, 2, 3, 4]
        <- ^ ->


-1 ->  1 * 0 = 0
1  -> -1 * 0 * -3 * 3 = 0
0  -> -1 * 1 * -3 * 3 = 9
-3 -> 0
3  -> 0

Questions:
    - Sorted?
    
Intuition :
    - prefix sum of all other numbers at an array
    - the

'''