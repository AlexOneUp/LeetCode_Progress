class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0
        
        max_heap = [-a, -b, -c]
        
        heapq.heapify(max_heap)
        
        while True :
            if max_heap[0] != 0 and max_heap[1] != 0:
                res += 1
#                 Pop from the first 2 values aka pops right
                first = heapq.heappop(max_heap)
                
                second = heapq.heappop(max_heap)

                heapq.heappush(max_heap, first + 1)
                heapq.heappush(max_heap, second + 1)
            else : 
                break
        return res 