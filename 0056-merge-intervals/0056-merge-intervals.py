class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by the first values of each interval, so we can have a sorted list
        intervals.sort(key=lambda x: x[0])
        
        # merged intervals will begin with the first element
        res = [intervals[0]]
        for interval in intervals:
            # if c is <= b, then the intervals overlap
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res
        
        
'''
Intuition
    - We know the intervals are sorted already?
        Since they're sorted, we can pretty much merge them into an interval.
        We would just have to find the overlapping ones
    - What does 'merge' mean?
        - combining overlapping intervals into a single inteval
            i.e [1,3] + [2, 6] = [1,6]
    - how to know if intervals overlap?
        [a,b] + [c,d] = [a, d], if c <= b
    - what to do when overlap?
        - merge by :
            - [a, max(b, d)]
    - if they don't overlap :
        - add current interval to list of results
        
1. 
'''