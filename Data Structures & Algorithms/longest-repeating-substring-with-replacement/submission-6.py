class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # So I think the idea is that we should have a sliding window where we keep track of the characters collected so far and  subtract it with the most repeated character and if the are exceeding the k value, thenw e reduce the window and reduce the character count in the dictioanry
        longest_sub = 0
        char_count = {}
        window_origin = 0
        for i , c in enumerate(s):
            window_size = i - window_origin + 1
            char_count[c] = char_count.get(c , 0) + 1
            most_repeated_char = max(char_count.values())
            if window_size - most_repeated_char > k:
                # Reduce the window
                char_count[s[window_origin]] -= 1
                window_origin += 1
            else:
                longest_sub = max(longest_sub , window_size)
        return longest_sub
