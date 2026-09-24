class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals , key = lambda interval: interval[0])
        print(sorted_intervals)
        merged_intervals = []
        l =0 
        r = l
        while r < len(sorted_intervals):
            start = sorted_intervals[l][0]
            end = sorted_intervals[l][1]
            while r < len(sorted_intervals) and end >= sorted_intervals[r][0]: #This means that there is overlapping  
                end = max(sorted_intervals[r][1] , end)
                r += 1
            result = [start , end]
            merged_intervals.append(result)
            l = r

        return merged_intervals
        
            