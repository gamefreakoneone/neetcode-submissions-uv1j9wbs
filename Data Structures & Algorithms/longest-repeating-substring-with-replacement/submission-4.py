class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count= {}
        most_repeated_char = ""
        i , longest = 0, 0
        for j , ch in enumerate(s):
            char_count[ch] = char_count.get(ch , 0) + 1
            # most_repeated_char = max(char_count , key=char_count.key())
            most_repeated_val = max(char_count.values())
            window = j - i + 1
            replacement = window - most_repeated_val
            if replacement  <= k : # Time to replace
                longest = max(longest, window)

            while replacement > k:
                char_count[s[i]] -= 1
                i += 1
                most_repeated_val = max(char_count.values())
                window = j - i + 1
                replacement = window - most_repeated_val
        
        return longest