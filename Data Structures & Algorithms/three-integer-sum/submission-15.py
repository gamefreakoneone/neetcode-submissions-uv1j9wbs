class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i , num in enumerate(nums):
            if num > 0: # Since at this point we cannot make a compliment
                break 
            
            if i > 0 and nums[i-1] == num:
                continue # Skipping duplicates

            j , k = i+1 , len(nums)-1

            while j < k:
                target = nums[i]+nums[j]+nums[k]
                if target <0:
                    j += 1
                elif target > 0:
                    k -= 1
                else:
                    result.append([ nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j]==nums[j-1] :
                        j+=1
                    while k >0  and nums[k]== nums[k+1] :
                        k-=1

        
        return result