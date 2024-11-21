class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
#         l, r = 0, 1
#         subarr_sz = set()
#         while r < len(nums) + 1:
            
#             while r < len(nums) and nums[r] > nums[r-1] and r - l + 1 <= k:
#                 r += 1
#         if r - l == k:
#             if (r - 1) in subarr_sz: return True
#             subarr_sz.add(r - 1)
#         l += 1
#         r = l + 1
#         return False
        # i is start of the current window
        i, j = 0, 1

        # Set to store indices of the ends of valid subarrays
        valid_ends = set() 

        while j < len(nums) + 1:

            # Expand the window only if its strictly increasing and within size k
            while j < len(nums) and nums[j] > nums[j-1] and j - i + 1 <= k:
                j += 1

            # If the just processed window is valid (of size k)
            if j - i == k:
                 # If there's an adjacent valid subarray before the current one
                if (i - 1) in valid_ends:
                    return True
                valid_ends.add(j - 1)
                
            # Update pointers for next subarray
            i += 1
            j = i + 1

        return False
'''
Intuition
    - 2 adjacent subarrays of length k

UMPIRE :
    - get the 2 adj subarrays of len k 
    - within N length array
    
M :
    - sliding window approach
        + sliding window of length k
P:
    - example :
        [2,5,7,8,9,2,3,4,3,1], k = 3
         l r
        + slide the right ptr if [right element - 1] is exactly 1 more than itself
            ++ do this until (r - l + 1) == k
        + append the subarray to a set
        + if the subarray size is 2, return true
        + else return false
'''