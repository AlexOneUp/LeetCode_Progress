class RandomizedSet:

    def __init__(self):
        # track number and the 
        self.hmap = {}
        self.arr = []

        
        
    def insert(self, val: int) -> bool:
        bool_inMap = val not in self.hmap
        
        if bool_inMap: 
            self.hmap[val] = len(self.arr)
            self.arr.append(val)
    
        return bool_inMap

    def remove(self, val: int) -> bool:
        bool_inMap = val in self.hmap
        
        if bool_inMap:
            idx = self.hmap[val]
            lastVal = self.arr[-1]
            self.arr[idx] = lastVal
            self.arr.pop()
            self.hmap[lastVal] = idx
            del self.hmap[val]
        return bool_inMap
            
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()