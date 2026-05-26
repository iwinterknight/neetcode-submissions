class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        merged = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], e)]
            else:
                merged.append([s, e])
        
        return merged