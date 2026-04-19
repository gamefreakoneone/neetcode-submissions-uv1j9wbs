class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j = 0 , 0
        curr_track = {}
        longest_con = 0 
        while j < len(s):
            if (s[j] not in curr_track.keys()) or curr_track[s[j]] == 0:
                curr_track[s[j]] = 1
                j += 1
            elif curr_track[s[j]] == 1:
                curr_con = j - i
                longest_con = max(longest_con , curr_con)
                while curr_track[s[j]] == 1:
                    curr_track[s[i]] -= 1
                    i += 1
        longest_con = max(longest_con , j - i)
        return longest_con