class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        prev = float('-inf')
    # Step 2: Iterate through the intervals and check for overlap.
        for i in range(len(intervals) - 1):
            # Compare the end time of the current interval with the start time of the next interval.
            if intervals[i][1] > intervals[i + 1][0]:
                return False  # Found an overlap, so return False.
        
        return True
'''
Meeting 
if the meetings overlap, then return false

otherwise continue return true


Intuition
We have a list of intervals
A person should be able to attend all meetings
A person can only be at one meeting at a time
So there must not be any overlaps
We need to check whether or not if we find any overlaps
'''