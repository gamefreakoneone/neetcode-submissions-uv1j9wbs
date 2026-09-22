class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChar = set()
        l = 0
        longest = 0
        for i, c in enumerate(s):
            if c in visitedChar:
                while c in visitedChar:
                    visitedChar.remove(s[l])
                    l += 1
            visitedChar.add(c)
            longest = max(longest , i - l + 1)
        
        return longest

