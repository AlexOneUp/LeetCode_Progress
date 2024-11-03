class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge = []
        
        res = []
        

        for i in range(len(intervals)):
            start, end = newInterval[0], newInterval[1]
            # end < b
            if end < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # b < start
            elif start > intervals[i][1]:
                res.append(intervals[i])
                
            else:
                newInterval = [min(start, intervals[i][0]), max(end, intervals[i][1])]
        res.append(newInterval)   
        
#         for interval in intervals:
#             if :
#             # (interval[0] <= start and start <= interval[1]) or (interval[0] <= end and end <= interval[1]):
#                 merge.append(interval)
#             else: 
#                 res.append(interval)

#         for interval in merge:
#             start = min(start, interval[0])
#             end = max(end, interval[1])
#             merge.pop()
#         merge.append([start, end])

        # for interval in intervals:
            
        return res
    
        
'''
       
[
 [1,2],[3,5],[6,7],[8,10],[12,16]     
]
insert [4,8]

u can have multiple overlapping intervals

Visual 
[0          5         10        15          20]
   1->2
        3-->5
              6->7
                  8-->10
                           12----->16
insert [4,8]                           
          4------>8 
          
  [1, 2][3             10] [12      16]
       
       
       
Intuition :
    - keep track of the start and end values of the inserted interval
        its overlapping if:
        say 3,5 = a,b and 6,7 = c,d and 8,10 = e,f  
            if (start <= b and start >= a) OR (end <= b and end >= a), append the interval into a list to compare later
                - (a <= start <= b) OR (a <= end <= b) append the interval
        
            
    -
       
'''