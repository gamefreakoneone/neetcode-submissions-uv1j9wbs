class Solution:
    def countSubstrings(self, s: str) -> int:
        n , res = len(s) , 0
        dp = {}
        for i in range(n-1 , -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i <=2 or (i+1 , j-1) in dp):
                    dp[(i,j)] = True
                    res += 1

        return res