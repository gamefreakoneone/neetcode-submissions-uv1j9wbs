class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_dict= {}
        i , longest = 0 , 0
        for j , ch in enumerate(s):
            if ch in check_dict and i <= check_dict[ch]: 
                i = check_dict[ch] + 1
            check_dict[ch] = j
            longest = max(longest, j - i + 1)
            j += 1       
        return longest