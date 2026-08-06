class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for word in strs:
            len_word = len(word)
            result += str(len_word) + "*" + word
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded = []
        i = 0
        j = len(s)
        while i < j:
            k = i
            while s[k].isalnum():
                k+=1
            len_word = int(s[i:k])
            word_start = k+1
            word = s[word_start : word_start + len_word ]
            decoded.append(word)
            i = word_start + len_word 
        return decoded