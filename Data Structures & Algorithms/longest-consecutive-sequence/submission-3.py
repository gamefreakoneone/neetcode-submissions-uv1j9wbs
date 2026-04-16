class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        available_nums = {}
        largest_number = nums[0]
        smallest_number = nums[0]
        
        for i in nums:
            if i > largest_number:
                largest_number = i
            elif i < smallest_number:  # else if -> elif
                smallest_number = i
            available_nums[i] = True
        
        longest_cons = 0
        current_cons = 0
        for i in range(smallest_number, largest_number + 1):
            if i in available_nums:  # use `in` to avoid KeyError
                current_cons += 1
                longest_cons = max(longest_cons, current_cons)
            else:
                current_cons = 0
        
        return longest_cons