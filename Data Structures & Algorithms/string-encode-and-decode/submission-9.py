class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for word in strs:
            len_word = len(word)
            encoded_word = str(len_word) + "*"+ word
            result += encoded_word
        
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        words=[]
        len_string = len(s)
        i = 0
        j = i
        while j < len_string:
            if s[j].isdigit():
                j += 1
            elif s[j]=='*':
                number = int(s[i:j])
                i = j+1
                j = i+number
                word = s[i:j]
                words.append(word)
                if j < len_string:
                    i = j
                    

        return words

