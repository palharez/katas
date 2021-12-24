class Solution:
    """
    difficult: Medium

    Given an array of intervals where intervals[i] = [starti, endi], 
    merge all overlapping intervals, and return an array of the non-overlapping 
    intervals that cover all the intervals in the input.

    Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
        

    Constraints:
        1 <= intervals.length <= 104
        intervals[i].length == 2
        0 <= starti <= endi <= 104
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        last_start = -1
        last_end = 0

        overlappings = []

        for start, end in intervals:
            if last_start == -1:
                last_start = start
                last_end = end
                continue

            if start <= last_end:
                if last_start > start:
                    last_start = start
                
                if last_end < end:
                    last_end = end

                continue

            if start > last_end:
                overlappings.append([last_start, last_end])
                last_start = start
                last_end = end
                continue
        
        overlappings.append([last_start, last_end]) # To add the last interation
        
        return overlappings