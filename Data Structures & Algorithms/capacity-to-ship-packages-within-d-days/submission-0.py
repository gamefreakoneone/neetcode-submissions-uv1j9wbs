class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        result = r
        #Here day and ship is interchangable
        while l <=r:
            mid_cap = (l+r)//2
            ship = 1
            curr_cap = mid_cap

            for weight in weights:
                if curr_cap - weight >= 0 :
                    curr_cap -= weight
                else:
                    ship += 1
                    curr_cap = mid_cap - weight
            
            if ship <= days:
                result = min(result , mid_cap)
                r = mid_cap - 1
            else:
                l = mid_cap+1

        return result