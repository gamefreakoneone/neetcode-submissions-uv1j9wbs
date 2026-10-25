class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # The ending of the new interval is less than start of the next interval
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # The start of the new interval is more than the ending of the prev interval
                result.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0] , intervals[i][0]),
                    max(newInterval[1] , intervals[i][1])
                ]

        result.append(newInterval)
        return result