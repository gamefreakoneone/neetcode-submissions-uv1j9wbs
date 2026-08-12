class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals
        intervals.sort(key = lambda i : i[0])
        outputs = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= outputs[-1][1]:
                temp_end = max(outputs[-1][1] , end)
                outputs[-1][1] = temp_end
                # outputs.append([start, temp_end])
            else:
                outputs.append([start, end])

        return outputs
        