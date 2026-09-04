class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M , N = len(text1) , len(text2)
        cache = [[None] * N for _ in range(M) ]
        
        def dfs(text1 , text2, l1, l2, cache):
            if l1 == M or l2==N:
                return 0
            if cache[l1][l2] != None:
                return cache[l1][l2]

            if text1[l1]==text2[l2]:
                cache[l1][l2] = 1+ dfs(text1, text2, l1+1 , l2+1, cache)
            else :
                cache[l1][l2] = max(dfs(text1, text2, l1+1 , l2, cache) , dfs(text1, text2, l1 , l2+1, cache))

            return cache[l1][l2]
        longest = dfs(text1, text2, 0, 0, cache)
        return longest