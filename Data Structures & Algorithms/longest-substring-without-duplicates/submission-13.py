class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        l = 0
        for i , c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
            max_length = max(max_length , i - l + 1 )
            seen.add(c)
        
        return max_length