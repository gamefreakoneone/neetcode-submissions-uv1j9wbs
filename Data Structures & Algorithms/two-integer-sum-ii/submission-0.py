class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers) - 1
        result= []
        while l < r:
            if numbers[l] + numbers[r] == target:
                result.append(l+1)
                result.append(r+1)
                return result
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        
        return None
