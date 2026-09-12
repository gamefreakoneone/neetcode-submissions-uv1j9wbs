class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            expected_result = target - nums[i]
            if expected_result in store:
                return [store[expected_result] , i] 
            store[nums[i]] = i
        return []