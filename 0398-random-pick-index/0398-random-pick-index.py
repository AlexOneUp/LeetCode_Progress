class Solution:

    def __init__(self, nums: List[int]):
        self.indices = {}
        
        # Adj List - Store lookups of the list of indexes into the value
        for idx, num in enumerate(nums):
            if num not in self.indices: 
                self.indices[num] = [idx]
            else: 
                self.indices[num].append(idx)
        print(self.indices)

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# Probability question :
# Random weight usually means :
#   There should be an equal probability that there exists a target #
# We can store lookups in a hmap to record the picked #, and return a index