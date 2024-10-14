class MyHashMap:

    def __init__(self):
        #Limit is 1000 size and each bucket inits with None
        self.size = 10**3
        self.buckets = [[] for _ in range(self.size)]
        
    
    def hash_func(self, key):
        # The hash function is usually calculated by 
        # returns the hash function
        # Hash Function : key % size
        return key % self.size
    
    # void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    def put(self, key: int, value: int) -> None:
        #compute hash index
        hash_idx = self.hash_func(key)

        # check if key, val pairs present in bucket
        for pair in self.buckets[hash_idx]:
            if pair[0] == key:
                # print(pair)
                pair[1] = value
                return
            
        #if key isnt found, append the (k, v) pair
        self.buckets[hash_idx].append([key, value])
        

    # int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    def get(self, key: int) -> int:
        hash_idx = self.hash_func(key)
        for pair in self.buckets[hash_idx]:
                if key == pair[0]:
                    return pair[1]
        return -1

    # void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

    def remove(self, key: int) -> None:
        hash_idx = self.hash_func(key)
        for pair in self.buckets[hash_idx]:
                if key == pair[0]:
                    self.buckets[hash_idx].remove(pair)
                    return
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)