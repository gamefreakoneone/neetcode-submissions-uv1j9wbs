class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_longest = 0
        length = 0
        for num in nums:
            if num - 1 not in num_set:
                length += 1 
                while num + 1 in num_set:
                    num += 1
                    length += 1
            max_longest = max(max_longest, length)
            length = 0
        return max_longest
