class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} # Stores value -> index
        for i , num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement] , i]
            num_dict[num] = i # i is the index
        