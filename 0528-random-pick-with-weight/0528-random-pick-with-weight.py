class Solution:

    def __init__(self, w: List[int]):
        # Prefix sums bascially says :
        # Input : [1,2,4] = 7 (total weight) and there are 1/7, 2/7, 4/7 chances to pick each index.
        # However, the probability is a range in length of input.
        self.prefix_sums = []
        
        total = 0
        
        for weight in w:
            total+= weight
            self.prefix_sums.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # The random weight range picker
        target = random.uniform(0, self.total)
        
        # Binary search to check whether the ranges is within the window
        l = 0
        r = len(self.prefix_sums)
        # The remaining answer should eval to the left pointer
        while l < r:
            mid = (l + r) // 2
            
            # If the midpt is < than random weight
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()