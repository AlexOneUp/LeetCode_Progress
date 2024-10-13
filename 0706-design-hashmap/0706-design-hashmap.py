class MyHashMap:

    def __init__(self):
        # Initialize a list with 1000 empty buckets
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key):
        # Hash function to determine the bucket index
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        # Insert key-value pair into HashMap
        hash_key = self.hash(key)
        # Check if the key already exists, if so, update the value
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][i] = (key, value)
                return
        # If key doesn't exist, append the new key-value pair
        self.buckets[hash_key].append((key, value))

    def get(self, key: int) -> int:
        # Return the value for the given key, or -1 if it doesn't exist
        hash_key = self.hash(key)
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        # Remove the key-value pair if it exists
        hash_key = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                del self.buckets[hash_key][i]
                return
      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)