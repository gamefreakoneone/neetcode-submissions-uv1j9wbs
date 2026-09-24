class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval : interval[0])
        merged_intervals = []
        for s, e in intervals:
            if merged_intervals and merged_intervals[-1][1] >= s:
                merged_intervals[-1][1] = max( merged_intervals[-1][1] , e)
            else:
                merged_intervals.append([s,e])

        return merged_intervals