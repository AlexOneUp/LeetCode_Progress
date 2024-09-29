class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        count = {x: nums.count(x) for x in set(nums)}
        freq = [[] for n in range(len(nums) + 1)]

        # Bucket sorting to store the occurences
        for num, c in count.items():
            freq[c].append(num)
        
        # print(freq)
        top_k = k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if top_k != 0:
                    res.append(n)
                    top_k -= 1 
        return res

