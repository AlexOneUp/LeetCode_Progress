class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1
        if len(intervals) == 1 : return 1
        # O(nlogn) 
        # sorting by start times
        intervals.sort(key=lambda x: x[0])
        
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # If intervals overlap
            if min_heap[0] <= intervals[i][0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i][1])
        
        return len(min_heap)
        
'''
min conf rooms required

if intervals overlap, new meeting rooms required
overlapping intervals : for [a, b] and [c, d], c <= b

min meeting rooms is 1
keyword minimum # conference rooms

i can use a min heap


visual representation :
[0                            30]
    [5, 10] 
                [15,20]

'''
        