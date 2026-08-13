class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_dict = {} # THe indices are numbers and the values are indices
        for i , num in enumerate(nums):
            complement = target - num
            if complement in checked_dict: # Searches for the keys, not values
                return [checked_dict[complement] , i] # Since they asked to return the sammer index first
            checked_dict[num] = i