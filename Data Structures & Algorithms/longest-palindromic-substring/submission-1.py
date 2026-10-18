class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        result = ""

        def helper(l ,r):
            nonlocal max_length , result
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_length:
                    max_length = max(max_length , r-l+1)
                    result = s[l:r+1]
                l-=1
                r+=1

            
        
        for i in range(len(s)):
            # If the substring is odd
            helper(i,i)

            # If the substring is event
            helper(i, i+1)

        return result

        