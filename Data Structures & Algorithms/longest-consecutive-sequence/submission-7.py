class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        min = float('inf')
        max = - float('inf')
        # for num in set_nums:
        #     if num <= min:
        #         min = num
        #     if num > max:
        #         max = num
        
        conc = 1
        longest_conc = 0

        for num in set_nums:
            if num - 1  not in set_nums: # We are only coutnign when we have a starting point not midway
                conc = 1
                while num + conc in set_nums:
                    conc += 1
                if conc > longest_conc:
                    longest_conc = conc
        return longest_conc
