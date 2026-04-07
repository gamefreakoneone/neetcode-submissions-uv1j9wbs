class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked= []
        for i in nums:
            if i in checked:
                return True
            checked.append(i)
        return False