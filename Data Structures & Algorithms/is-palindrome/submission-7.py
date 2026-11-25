class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = [ c.lower() for c in s if c.isalnum()]
        return characters ==  characters[::-1]