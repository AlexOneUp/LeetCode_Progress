class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        in_hmap = val in self.hmap
        
        if not in_hmap:
            self.hmap[val] = len(self.arr)
            self.arr.append(val)       
        return not in_hmap

    def remove(self, val: int) -> bool:
        in_hmap = val in self.hmap
        
        if in_hmap:
            idx = self.hmap[val]
            last_val = self.arr[-1]
            self.arr[idx] = last_val
            self.arr.pop()
            self.hmap[last_val] = idx
            del self.hmap[val]    
        return in_hmap

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()