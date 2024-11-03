class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        
        for i in range(len(intervals) - 1):
            if intervals[i][1] <= intervals[i+1][0]:
                continue
            else: return False
        return True
        
'''
Intuition :
    [a, b], [c, d]
    if interval :
        if they overlap, compare c and b
            if c <= b, then they overlap
        usually is if d < b
        not an interval
    

'''