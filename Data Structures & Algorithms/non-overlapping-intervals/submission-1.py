class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, n):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res
