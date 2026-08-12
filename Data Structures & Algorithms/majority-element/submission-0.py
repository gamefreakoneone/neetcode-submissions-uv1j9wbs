class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        chosen_num = None
        count = 0
        for i in nums:
            if count == 0:
                chosen_num = i
            if i != chosen_num:
                count -= 1
            else:
                count  += 1
        return chosen_num