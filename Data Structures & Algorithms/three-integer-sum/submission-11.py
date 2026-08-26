class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)- 2):
            low , high = i + 1, len(nums) - 1
            if nums[i] > 0:  # We are in the positive range, adn we wont find a compliment
                break
            if (i > 0 and nums[i]==nums[i-1]):
                continue
            
            while low < high:
                result = nums[i] + nums[low] + nums[high]
                if result < 0:
                    low += 1
                elif result >0:
                    high -=1
                else:
                    results.append([nums[i] , nums[low] , nums[high]])
                    low += 1
                    high -=1
                    while low < high and nums[low] == nums[low-1]:
                        low+=1
                    while low <high and nums[high] == nums[high + 1]:
                        high -= 1
        
        return results