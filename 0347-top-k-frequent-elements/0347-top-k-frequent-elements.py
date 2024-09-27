class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        freq = {x: nums.count(x) for x in set(nums)}
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        res=[]
        top_k_counter = k
        for key, val in sorted_freq.items():
                if top_k_counter == 0 :
                    break
                else:
                    res.append(key)
                
                top_k_counter-=1
 
        return res
