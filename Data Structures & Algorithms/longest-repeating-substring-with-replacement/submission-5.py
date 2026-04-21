class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        i, longest = 0, 0

        for j, ch in enumerate(s):
            char_count[ch] = char_count.get(ch, 0) + 1
            most_repeated_val = max(char_count.values())
            window = j - i + 1

            if window - most_repeated_val > k:
                char_count[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)

        return longest