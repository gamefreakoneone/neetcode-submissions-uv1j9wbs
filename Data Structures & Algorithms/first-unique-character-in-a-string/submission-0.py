class Solution:
    def firstUniqChar(self, s: str) -> int:
        countedChar = Counter(s)
        for i , c in enumerate(s):
            if countedChar[c]==1:
                return i
        return -1