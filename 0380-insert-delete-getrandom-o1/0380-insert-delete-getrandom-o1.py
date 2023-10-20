class RandomizedSet:

    def __init__(self):
        self.map_idx = {}
        self.list_nums = []

    def insert(self, val: int) -> bool:
        val_in_map = val in self.map_idx
        # Populate the hashmap if the val is not in the hashmap already
        if not val_in_map: 
            self.map_idx[val] = len(self.list_nums)
            self.list_nums.append(val)
        return not val_in_map

    def remove(self, val: int) -> bool:
        val_in_map = val in self.map_idx
        
        # Pointer magic
        if val_in_map:
            idx = self.map_idx[val]
            last_val = self.list_nums[-1]
            self.list_nums[idx] = last_val
            # Removing actual last element
            self.list_nums.pop()
            
            # Update the hashmap val with the new idx
            self.map_idx[last_val] = idx
            # Remove the previous val from our hmap
            del self.map_idx[val]
        return val_in_map
    
    def getRandom(self) -> int:
        return random.choice(self.list_nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()