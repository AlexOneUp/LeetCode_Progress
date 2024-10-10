class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

#         while l <= r:
#             m = l + ((r - 1) // 2)
   
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1
    
        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1