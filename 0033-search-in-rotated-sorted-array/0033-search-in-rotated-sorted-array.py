class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 

        while l <= r:
            m = l + (r - l) // 2
            
            
            if target == nums[m]: return m
            
            #Check left sorted
            if nums[l] <= nums[m]:
                # check if targets within the range of this left section
                if nums[l] <= target < nums[m]:
                    
                    r = m - 1
                else: 
                    l = m + 1
            # Check right sorted
            else:
                # check if targets within range of right section
                if nums[m] < target <= nums[r]:
                    l = m +1
                else: 
                    r = m -1
            
            
            
        return -1
        
        
''' 
Write in log n runtime

Intuition :
    - Array can be rotated K times <= nums len
        - Arrays already sorted in ascending order
        - Target is given
        - not given k   
            - **K is always positive**
            - elements can be -/+
            
    - Bin Search 
        to look in elements in log n time
        how should we determine a mid point?
            do BS as usual
            check if left is sorted, check if rights sorted
                update mid if they arent sorted


'''