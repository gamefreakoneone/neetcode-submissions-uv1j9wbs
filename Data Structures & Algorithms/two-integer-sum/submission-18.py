class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i in range(len(nums)):
            calc = target - nums[i]
            if calc in prev:
                return [prev[calc] , i]
            prev[nums[i]] = i
        