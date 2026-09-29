class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_intervals = sorted(intervals , key = lambda x : x[0])
        result = []
        for s , e in sort_intervals:
            if result and result[-1][1] >= s:
                result[-1][1] = max(result[-1][1] , e)
            else:
                result.append([s,e])
        
        return result