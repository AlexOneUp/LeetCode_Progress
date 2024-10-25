class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the intervals by the starting values.
        intervals.sort(key=lambda x: x[0])

        # List to hold merged intervals.
        merged = []

        for interval in intervals:
            # If merged is empty or there is no overlap with the last interval in merged, add it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so merge the current interval with the last one in merged.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
